from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company, Skill, Master, Order
from rest_framework.fields import CurrentUserDefault


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'url', 'username', 'email', 'groups'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = 'pk', 'user', 'skills', 'url'


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.CharField(default=serializers.CurrentUserDefault())
    service_url = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = 'client', 'service', 'executor', 'execution_date', 'service_url'
        extra_kwargs = {
            'executor': {'required': True},
            # 'execution_date': {'required': True},
        }


