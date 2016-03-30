# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_imageslogo_img_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageslogo',
            name='img_src',
            field=models.CharField(max_length=300),
        ),
    ]
