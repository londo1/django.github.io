# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 12:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendorInterface', '0005_auto_20170913_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promotion',
            old_name='promotionID',
            new_name='promotion_id',
        ),
    ]