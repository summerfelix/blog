# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-04 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('tags', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('operate_time', models.DateTimeField(auto_now=True, null=True)),
                ('icon', models.ImageField(null=True, upload_to='article')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
