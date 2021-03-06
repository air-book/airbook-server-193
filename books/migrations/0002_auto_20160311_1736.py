# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-11 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcategory',
            options={'ordering': ['tags']},
        ),
        migrations.RemoveField(
            model_name='bookcategory',
            name='order',
        ),
        migrations.AddField(
            model_name='bookcategorytype',
            name='cat_type',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='tags',
            field=models.CharField(help_text=b'Aggiungere massimo 3 Tags', max_length=16),
        ),
    ]
