# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-10 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0016_auto_20180411_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='VP_Recruitment_Information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VP_Recruitment_Information', to='general.Sister'),
        ),
    ]