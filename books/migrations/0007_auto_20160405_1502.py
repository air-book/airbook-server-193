# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-05 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20160311_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='bookauthor',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='bookcategorytype',
            name='icon',
        ),
        migrations.AddField(
            model_name='book',
            name='spessore',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Spessore'),
        ),
        migrations.AlterField(
            model_name='book',
            name='conditions',
            field=models.IntegerField(blank=True, choices=[(0, b'Pessimo'), (1, b'Accettabile'), (2, b'Buono'), (3, b'Ottimo'), (4, b'Nuovo')], null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='heigth',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Altezza'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title_art',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='weigth',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Peso'),
        ),
        migrations.AlterField(
            model_name='book',
            name='width',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Larghezza'),
        ),
        migrations.AlterField(
            model_name='bookauthor',
            name='name',
            field=models.CharField(blank=True, help_text=b'Inserire il nome ed il cognome dellautore', max_length=200, null=True),
        ),
    ]
