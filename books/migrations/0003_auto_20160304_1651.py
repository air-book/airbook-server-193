# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160304_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category_type',
            field=models.ManyToManyField(to='books.BookCategoryType'),
        ),
    ]