# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcategorytype',
            name='category_type',
            field=models.CharField(blank=True, choices=[(b'PRIMA EDIZIONE', b'Prima Edizione'), (b'EDIZIONE ECONOMICA', b'Edizione Economica'), (b'LIBRO ANTICO', b'Libro Antico 400'), (b'LIBRO ANTICO', b'Libro Antico 500'), (b'LIBRO ANTICO', b'Libro Antico 600'), (b'LIBRO ANTICO', b'Libro Antico 700'), (b'LIBRO ANTICO', b'Libro Antico 800'), (b'LIBRO AUTOGRAFATO', b'Libro Autografato'), (b'LIBRO D ARTISTA', b'Libro d Artista')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='volumes_type',
            field=models.IntegerField(choices=[(0, b'Raccolta di n volumi'), (1, b'Volume Singolo')]),
        ),
    ]
