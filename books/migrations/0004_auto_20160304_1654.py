# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160304_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='altri_canali',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
