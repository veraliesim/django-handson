# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storedetails',
            fields=[
                ('id', models.IntegerField(blank=True, db_column='ID', primary_key=True, serialize=False)),
                ('store_name', models.CharField(blank=True, db_column='Seller_name', max_length=1000, null=True)),
                ('store_location', models.CharField(blank=True, db_column='Website', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'StoreDetails',
                'managed': False,
            },
        ),
    ]
