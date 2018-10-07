from django.urls import reverse
from django.contrib.auth.models import User
from re import search
from ..serializers import OrderSerializer
from ..models import Master, Order
from ..views import MasterViewSet, OrderViewSet, UserViewSet
from .factories import MasterFactory, OrderFactory, UserFactory
from rest_framework.test import (APITestCase, force_authenticate,
                                 APIRequestFactory)


class OrdersListTestCase(APITestCase):
    url = reverse('order-list')
    view = OrderViewSet.as_view({'get': 'list'})

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
            master_url = reverse('master-detail', args=(master.pk,))
            master_request = factory.get(master_url)
            master_view = MasterViewSet.as_view({'get': 'retrieve'})
            force_authenticate(master_request, user=master.user)
            master_response = master_view(master_request, pk=master.pk)
            master_link = master_response.data['url']

            force_authenticate(request, user=master.user)
            response = view(request)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.data), 2)
            for order in response.data:
                self.assertEqual(order['executor'], master_link)

    def test_clients_orders(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = OrderViewSet.as_view({'get': 'list'})
        masters = Master.objects.all().values_list('user__pk', flat=True)

        for user in User.objects.all():
            if user.pk in masters:
                continue
            else:
                user_url = reverse('user-detail', args=(user.pk,))
                user_request = factory.get(user_url)
                user_view = UserViewSet.as_view({'get': 'retrieve'})
                force_authenticate(user_request, user=user)
                user_response = user_view(user_request, pk=user.pk)
                user_link = user_response.data['url']

                force_authenticate(request, user=user)
                response = view(request)
                self.assertEqual(response.status_code, 200)

                for order in response.data:
                    self.assertEqual(order['client'], user_link)

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


