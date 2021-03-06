# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=200)),
                ('count_product', models.IntegerField(default=0)),
                ('destination_adress', models.CharField(max_length=200)),
                ('date_delivery', models.DateTimeField(verbose_name='date delivery')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
