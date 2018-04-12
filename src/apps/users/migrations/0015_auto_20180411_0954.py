# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-11 09:54
from __future__ import unicode_literals

import apps.users.models.profile
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180404_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chief',
            name='email_confirmed',
            field=models.BooleanField(default=False, verbose_name='email_confirmed'),
        ),
        migrations.AlterField(
            model_name='chief',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='chief',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='chief',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=apps.users.models.profile.upload_file, verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='chief',
            name='second_name',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='second_name'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email_confirmed',
            field=models.BooleanField(default=False, verbose_name='email_confirmed'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=apps.users.models.profile.upload_file, verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='second_name',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='second_name'),
        ),
    ]
