# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20170713_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
