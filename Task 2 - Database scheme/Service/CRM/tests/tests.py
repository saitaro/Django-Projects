from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from django.db.models import Q
from json import dumps as json
import requests
from django.test import Client
from re import search
from ..models import Master, Order, Skill
from ..serializers import MasterSerializer, OrderSerializer, UserSerializer
from ..views import MasterViewSet, OrderViewSet, UserViewSet
from .factories import MasterFactory, OrderFactory, UserFactory
from factory import fuzzy
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import (APIRequestFactory, APITestCase,
                                 force_authenticate)

class OrdersListTestCase(APITestCase):
    url = api_reverse('order-list')
    # url_create = reverse('order-create')

    def setUp(self):
        master1, master2 = MasterFactory(), MasterFactory()
        order1_1, order1_2 = OrderFactory(executor=master1), OrderFactory(executor=master1)
        order2_1, order2_2 = OrderFactory(executor=master2), OrderFactory(executor=master2)
        self.assertEqual(Master.objects.count(), 2)
        self.assertEqual(Order.objects.count(), 4)
        self.assertEqual(User.objects.count(), 6)

    def test_masters_orders(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = OrderViewSet.as_view({'get': 'list'})

        for master in Master.objects.all():
            master_detail = reverse('master-detail', args=(master.pk,))
            master_request = factory.get(master_detail)
            master_data = MasterSerializer(master, context={'request': master_request}).data
            
            force_authenticate(request, user=master.user)
            response = view(request)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.data), 2)
            for order in response.data:
                self.assertEqual(order['executor'], master_data['url'])

    def test_clients_orders(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = OrderViewSet.as_view({'get': 'list'})
        masters = Master.objects.all().values_list('user__pk', flat=True)

        for user in User.objects.all():
            if user.pk in masters:
                continue
            else:
                force_authenticate(request, user=user)
                response = view(request)
                self.assertEqual(response.status_code, 200)

                for order in response.data:
                    self.assertEqual(order['client'], user.username)

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
        user = User.objects.create_user(username='Masha', password='12345')
        print(User.objects.all())
        client = Client()
        response = client.post(self.url, {'username': 'Masha', 'password': '12345'})
        print(response.status_code)


        # r = requests.get('127.0.0.1:8000' + self.url, auth=('user', 'pass'))
        # r.status_code


        # user = UserFactory()
        # print('USER IS:', user)
        # factory = APIRequestFactory()
        # # request = factory.post(self.url, data=None, format='json')
        # force_authenticate(self.client.request, user=user)


        # for order in Order.objects.all():
        #     print(order)

        # view = OrderViewSet.as_view({'post': 'create'})
        # user = User.objects.all()[0]

        # master = MasterFactory()
        # skill = Skill.objects.create(name='Cheeki-Breeki dance')
        # order = Order.objects.create(
        #     client=user,
        #     service=skill,
        #     executor=master,
        #     execution_date=datetime.now() + timedelta(days=1)
        # )


        # print(user, master, skill)
        # factory = APIRequestFactory()
        # order = OrderSerializer(order, context={'request':factory.post(self.url)}).data
        # # print(Order.objects.all())
        # request = factory.post(self.url, data=order, format='json')
        # force_authenticate(request, user=user)
        # print(request)
        # # print(master)
        # # response = self.client.post(self.url, data, format='json')

        # response = view(request)
        # print(response)


        # print(Order.objects.all())
        # print(Order.objects.filter(service=data['service']))
        # self.assertTrue(Order.objects.filter(Q()))