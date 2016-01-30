# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('side', '0003_auto_20160123_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='docfile',
            new_name='thumb',
        ),
        migrations.RemoveField(
            model_name='project',
            name='picture',
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
