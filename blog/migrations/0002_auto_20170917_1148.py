# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creative_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_data',
            new_name='published_date',
        ),
    ]
