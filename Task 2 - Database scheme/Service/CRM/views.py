from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets, filters
from django_filters import rest_framework
from .serializers import (UserSerializer, GroupSerializer, CompanySerializer,
                          MasterSerializer, SkillSerializer, OrderSerializer)


class PermissionFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user
        if user.is_authenticated:
            if user.is_staff:
                print(dir(queryset))
                return queryset.all()
            elif Master.objects.filter(user=user).exists():
                return queryset.filter(executor__user__username=user)
            else:
                return queryset.filter(client__username=user)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (PermissionFilterBackend,)
    # filterset_fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


