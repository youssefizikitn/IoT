# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('value', models.FloatField()),
                ('var', models.CharField(max_length=20)),
                ('unity', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('surface', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='capture',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='captures', to='receive.Room'),
        ),
    ]