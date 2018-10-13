from django.contrib.auth.models import User
from django.urls import reverse
from random import randint
from datetime import datetime, timedelta
from ..models import Master, Order, Skill
from ..serializers import OrderSerializer
from ..views import OrderViewSet
from .factories import MasterFactory, OrderFactory, UserFactory
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate


class OrdersListTestCase(APITestCase):
    url = api_reverse('order-list')

    def setUp(self):
        master1, master2 = MasterFactory(), MasterFactory()
        OrderFactory(executor=master1), OrderFactory(executor=master1)
        OrderFactory(executor=master2), OrderFactory(executor=master2)
        self.assertEqual(Master.objects.count(), 2)
        self.assertEqual(Order.objects.count(), 4)
        self.assertEqual(User.objects.count(), 6)

    def test_masters_orders(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = OrderViewSet.as_view({'get': 'list'})

        master = Master.objects.first()
        force_authenticate(request, user=master.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['executor'], master.pk)
        self.assertEqual(response.data[1]['executor'], master.pk)
            
        master = Master.objects.last()
        force_authenticate(request, user=master.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['executor'], master.pk)
        self.assertEqual(response.data[1]['executor'], master.pk)

    def test_clients_orders(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = OrderViewSet.as_view({'get': 'list'})
        masters = Master.objects.all().values_list('user__pk', flat=True)
        clients = User.objects.exclude(id__in=masters)
        
        user = clients[0]
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['client'], user.username)
        
        user = clients[1]
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['client'], user.username)

        user = clients[2]
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['client'], user.username)

        user = clients[3]
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['client'], user.username)

    def test_admin_access(self): 
        view = OrderViewSet.as_view({'get': 'list'})
        user = UserFactory(is_staff=True)
        factory = APIRequestFactory()
        request = factory.get(self.url)
        force_authenticate(request, user=user)
        response = view(request)
        orders = OrderSerializer(Order.objects.all(), many=True, context={'request': request})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, orders.data)
        
    def test_unauthorized_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['detail'], 
                         'Authentication credentials were not provided.')

    def test_user_post(self):
        order_count = Order.objects.count()
        user = User.objects.create_user(username='Masha')
        order = {
            'service': randint(1, Skill.objects.count()),
            'executor': randint(1, Master.objects.count()),
            'execution_date': datetime.now() + timedelta(days=1)
        }
        self.client.force_authenticate(user=user)
        response = self.client.post(self.url, order)
        self.assertEqual(Order.objects.count(), order_count + 1)
        new_order = Order.objects.last()
        self.assertEqual(new_order.client.username, user.username)
        self.assertEqual(new_order.service.pk, order['service'])
        self.assertEqual(new_order.executor.pk, order['executor'])
        self.assertEqual(new_order.execution_date.ctime(), order['execution_date'].ctime())
        

