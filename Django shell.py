# python manage.py shell

import django   
from django.apps import apps
django.setup()
models = apps.get_models()

print(models)
print(models[-1].objects.all())

# Delete all objects from the last model
models[-1].objects.all().delete()