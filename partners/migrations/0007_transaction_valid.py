# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-10 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0006_auto_20170625_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='valid',
            field=models.CharField(default='false', max_length=5),
            preserve_default=False,
        ),
    ]
