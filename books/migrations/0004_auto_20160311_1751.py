# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-11 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_bookcategorytype_category_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category_type',
            new_name='cat_type',
        ),
    ]