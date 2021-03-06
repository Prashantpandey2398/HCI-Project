# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-22 04:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=6)),
                ('contact', models.BigIntegerField(unique=True)),
                ('branch', models.CharField(choices=[('CSC', 'CSC'), ('CSE', 'CSE'), ('MEC', 'MEC'), ('CVL', 'CVL'), ('ECE', 'ECE')], max_length=6)),
                ('year', models.CharField(choices=[('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018')], max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
