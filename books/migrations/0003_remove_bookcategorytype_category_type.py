# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-11 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160311_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcategorytype',
            name='category_type',
        ),
    ]
