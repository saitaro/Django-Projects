from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from .models import Master, Order, Company, Skill
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.filters import BaseFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission, AllowAny
from django_filters import rest_framework
from .serializers import (UserSerializer, CompanySerializer, MasterSerializer,
                          SkillSerializer, OrderSerializer)


class PermissionFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user:
            user = request.user
            if user.is_staff:
                return queryset.all()
            elif Master.objects.filter(user=user).exists():
                return queryset.filter(executor__user__username=user)
            else:
                return queryset.filter(client__username=user)


class ClientPermission(IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user
        is_master = Master.objects.filter(user=user).exists()
        return not (is_master or user.is_staff)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (PermissionFilterBackend,)

    def get_permissions(self):
        if self.action in ['detail', 'list']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = IsAuthenticated, ClientPermission
        return [permission() for permission in permission_classes]

    # def create(self, request, *args, **kwargs):
    #     exclude = 'execution_date'
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # @permission_classes([IsAdminUser,])
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MasterViewSet(ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

    def get_master(self):
        return Master.objects.get(pk=self.pk)


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
