# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20170711_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.CharField(default=uuid.UUID('a971e616-995d-49c8-906e-3aedcb7ee6a2'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
