# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volume', '0002_auto_20150903_0814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='server',
            name='login',
            field=models.CharField(default=b'sellside', max_length=64),
        ),
        migrations.AlterField(
            model_name='server',
            name='password',
            field=models.CharField(default=b'Flex123!', max_length=64),
        ),
        migrations.AlterField(
            model_name='server',
            name='volumefolder',
            field=models.CharField(default=b'/home/sellside/fx-client-volumes/daily-rpts', max_length=256),
        ),
        migrations.AlterField(
            model_name='volume',
            name='server',
            field=models.CharField(max_length=64),
        ),
    ]
