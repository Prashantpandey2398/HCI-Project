# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-22 11:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0002_marksheets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marksheets',
            name='username',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Marksheets',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]