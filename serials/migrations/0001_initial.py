# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, default='American_dad')),
                ('serie', models.IntegerField()),
                ('episode', models.IntegerField()),
                ('url1', models.TextField()),
                ('url1_cc', models.IntegerField(default=0)),
                ('url2', models.TextField(default='')),
                ('url2_cc', models.IntegerField(default=0)),
                ('url1_cz', models.TextField(default='')),
                ('url2_cz', models.TextField(default='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Serials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, default='American_dad')),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.TextField(default='')),
                ('url1', models.CharField(max_length=400)),
                ('url2', models.CharField(max_length=400)),
                ('image', models.CharField(max_length=200)),
                ('title_cz', models.TextField(default='')),
                ('start_yr', models.IntegerField(default=0)),
                ('end_yr', models.IntegerField(default=0)),
                ('zaner', models.TextField(default='')),
                ('delka', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Topserials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, default='Brickleberry')),
                ('image', models.CharField(max_length=200, default='brickleberry_small.jpg')),
            ],
        ),
    ]
