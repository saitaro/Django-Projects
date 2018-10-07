from django.contrib.auth.models import User
from ..models import Master, Order, Skill, Company
import factory
from factory.django import DjangoModelFactory
from random import randint
from factory import fuzzy

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    
    username = factory.Faker('name')


class SkillFactory(DjangoModelFactory):
    class Meta:
        model = Skill
    
    name = factory.Faker('job')


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker('company')


class MasterFactory(DjangoModelFactory):
    class Meta:
        model = Master

    user = factory.SubFactory(UserFactory)
    company = factory.SubFactory(CompanyFactory)

    @factory.post_generation
    def skills(self, create, extracted, **kwargs):
        for _ in range(randint(1,4)):
            self.skills.add(SkillFactory())


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order
    
    client = factory.SubFactory(UserFactory)
    service = factory.SubFactory(SkillFactory)
    executor = factory.SubFactory(MasterFactory)
    
