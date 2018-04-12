# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_auto_20180212_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(default='', max_length=64, verbose_name='name')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
            ],
            options={
                'verbose_name_plural': 'food сosts',
                'verbose_name': 'food cost',
            },
        ),
        migrations.CreateModel(
            name='FoodTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start', models.TimeField(verbose_name='start')),
                ('end', models.TimeField(verbose_name='end')),
                ('type', models.CharField(choices=[('BREAKFAST', 'Завтрак'), ('BRUNCH', 'Обед'), ('DINNER', 'Ужин')], default='BREAKFAST', max_length=32, verbose_name='type')),
            ],
            options={
                'verbose_name_plural': 'FoodTimes',
                'verbose_name': 'food time',
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(default='', max_length=32, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'food types',
                'verbose_name': 'food type',
            },
        ),
        migrations.CreateModel(
            name='RoomFoodInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_food_info', to='hotels.FoodCost', verbose_name='cost')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_food_info', to='hotels.FoodType', verbose_name='type')),
            ],
            options={
                'verbose_name_plural': 'room food info',
                'verbose_name': 'room food info',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('abbreviation', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='abbreviation')),
                ('name', models.CharField(default='', max_length=32, verbose_name='name')),
                ('capacity', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='capacity')),
                ('english_name', models.CharField(default='', max_length=32, verbose_name='english name')),
                ('description', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='area',
            field=models.FloatField(default=0.0, verbose_name='area'),
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='rooms_count',
            field=models.IntegerField(default=1, verbose_name='rooms count'),
        ),
        migrations.AlterField(
            model_name='hotelroom',
            name='number',
            field=models.CharField(default='', max_length=16, verbose_name='number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='arrival_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='arrival date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='leave_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='leave date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('CONFIRMED', 'бронь подтверждена'), ('NOT_CONFIRMED', 'бронь не подтверждена'), ('OCCUPIED', 'занято')], default='NOT_CONFIRMED', max_length=32, verbose_name='payment status'),
        ),
        migrations.AddField(
            model_name='foodtime',
            name='room_food_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='times', to='hotels.RoomFoodInfo', verbose_name='room food info'),
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='food_info',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_info', to='hotels.RoomFoodInfo', verbose_name='room food info'),
        ),
    ]
