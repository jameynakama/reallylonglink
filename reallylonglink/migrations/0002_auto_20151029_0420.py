# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reallylonglink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reallylonglink',
            name='original_link',
            field=models.URLField(max_length=1000),
        ),
    ]
