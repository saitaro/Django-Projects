# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-03 21:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0002_remove_master_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='master',
            options={'verbose_name_plural': 'masterz'},
        ),
    ]