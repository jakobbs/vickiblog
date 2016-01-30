# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('side', '0004_auto_20160123_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumb',
            field=models.ImageField(upload_to='projectbilleder'),
        ),
    ]
