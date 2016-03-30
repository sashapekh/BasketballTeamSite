# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160318_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageslogo',
            name='description',
            field=models.TextField(default='Chicago bulls'),
        ),
    ]
