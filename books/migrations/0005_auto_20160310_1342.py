# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-10 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160304_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.BookCategory'),
        ),
    ]