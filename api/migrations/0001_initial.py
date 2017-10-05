# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bloodbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosp_name', models.TextField()),
                ('hosp_add', models.TextField()),
                ('hosp_contact', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('a_pos', models.IntegerField()),
                ('b_pos', models.IntegerField()),
                ('ab_pos', models.IntegerField()),
                ('o_pos', models.IntegerField()),
                ('a_neg', models.IntegerField()),
                ('ab_neg', models.IntegerField()),
                ('b_neg', models.IntegerField()),
                ('o_neg', models.IntegerField()),
            ],
        ),
    ]