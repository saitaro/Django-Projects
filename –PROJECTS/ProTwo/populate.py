import os
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User, Mail

fake = Faker()

def makeit(N):
    for i in range(N):

        first = fake.first_name()
        last = fake.last_name()
        mail = fake.email()

        new = User.objects.get_or_create(
            first_name = first,
            last_name = last
        )[0]

        Mail.objects.get_or_create(
            owner = new, 
            url = mail
        )[0]

if __name__ == '__main__':
    print('populating...')
    makeit(70)
    print('populating successfully completed.')