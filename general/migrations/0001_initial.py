# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_setup', models.BooleanField(default=False)),
                ('year_of_graduating_seniors', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-year_of_graduating_seniors'],
            },
        ),
        migrations.CreateModel(
            name='Sister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('class_year', models.IntegerField(default=0)),
                ('PRC', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AddField(
            model_name='setup',
            name='President',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='president', to='general.Sister'),
        ),
        migrations.AddField(
            model_name='setup',
            name='VP_CRS',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='VP_CRS', to='general.Sister'),
        ),
    ]
