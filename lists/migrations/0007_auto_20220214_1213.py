# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-02-14 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_remove_item_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='list',
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
