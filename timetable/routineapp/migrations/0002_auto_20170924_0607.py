# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routineapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='a',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='b',
            new_name='period',
        ),
    ]