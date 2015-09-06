# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('ipaddress', models.IPAddressField()),
                ('login', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('volumefolder', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='volume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'trade date')),
                ('time', models.TimeField(verbose_name=b'trade time')),
                ('side', models.CharField(max_length=8)),
                ('symbol', models.CharField(max_length=64)),
                ('bank', models.CharField(max_length=64)),
                ('size', models.IntegerField()),
                ('price', models.FloatField()),
                ('termsize', models.FloatField()),
                ('server', models.ForeignKey(to='volume.server')),
            ],
        ),
    ]
