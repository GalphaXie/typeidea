# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-06 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content_html'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='nv',
            new_name='uv',
        ),
    ]