# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20160818_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='create',
            new_name='created',
        ),
    ]
