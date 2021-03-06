# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-30 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_facebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='puntaje')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'db_table': 'app_facebook_user_score',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='userscores',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facebook.User'),
        ),
    ]
