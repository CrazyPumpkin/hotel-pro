# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 12:01
from __future__ import unicode_literals

import apps.common.models.country
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(blank=True, default='', max_length=4, null=True, verbose_name='code')),
                ('name', models.CharField(default='', max_length=32, verbose_name='name')),
                ('logo', models.ImageField(blank=True, default=None, null=True, upload_to=apps.common.models.country.upload_logo, verbose_name='logo')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'verbose_name': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('main', models.CharField(default='', max_length=32, verbose_name='main')),
                ('option', models.CharField(default='', max_length=8, verbose_name='option')),
            ],
            options={
                'verbose_name_plural': 'phones',
                'verbose_name': 'phone',
            },
        ),
    ]