# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-10 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20160310_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcategorytype',
            name='type',
        ),
    ]