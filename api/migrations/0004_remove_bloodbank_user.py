# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_bloodbank_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodbank',
            name='user',
        ),
    ]
