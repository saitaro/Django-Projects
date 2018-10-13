from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company, Skill, Master, Order
from rest_framework.fields import CurrentUserDefault


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = 'url', 'username', 'email', 'groups'


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        

class MasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Master
        fields = 'pk', 'user', 'skills', 'url'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.CharField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = 'client', 'service', 'executor', 'execution_date'
        extra_kwargs = {
            'executor': {'required': True},
            'execution_date': {'required': True},
        }


