# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 04:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_auto_20170802_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='Codigo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='Stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='StockMinimo',
            new_name='stockminimo',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='Unidad',
            new_name='unidad',
        ),
        migrations.RenameField(
            model_name='unidad',
            old_name='Descripcion',
            new_name='descripcion',
        ),
    ]
