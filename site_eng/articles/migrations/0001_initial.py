# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-14 08:52
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('author', models.CharField(max_length=20)),
                ('tags', models.CharField(max_length=100)),
            ],
        ),
    ]
