# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 02:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippets',
            new_name='Snippet',
        ),
    ]
