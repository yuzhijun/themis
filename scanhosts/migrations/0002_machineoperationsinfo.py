# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineOperationsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=0, verbose_name='\u64cd\u4f5c\u5e8f\u53f7')),
                ('person', models.CharField(default=b'', max_length=20, verbose_name='\u64cd\u4f5c\u4eba\u7528\u6237\u540d')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='\u64cd\u4f5c\u65f6\u95f4')),
                ('sn_key', models.CharField(unique=True, max_length=250, verbose_name='\u8bbe\u5907\u7684\u552f\u4e00\u6807\u8bc6')),
                ('machine_type', models.CharField(max_length=20, verbose_name='\u8bbe\u5907\u7c7b\u578b')),
                ('operation', models.TextField(default=b'', verbose_name='\u64cd\u4f5c\u5185\u5bb9', choices=[(0, b'\xe5\xa2\x9e\xe5\x8a\xa0'), (1, b'\xe5\x88\xa0\xe9\x99\xa4'), (2, b'\xe4\xbf\xae\xe6\x94\xb9')])),
                ('state', models.IntegerField(default=2, verbose_name='\u8bbe\u5907\u4f7f\u7528\u72b6\u6001', choices=[(0, b'\xe5\xb7\xb2\xe6\x8a\xa5\xe5\xba\x9f'), (1, b'\xe6\xb5\x8b\xe8\xaf\x95\xe4\xbd\xbf\xe7\x94\xa8'), (2, b'\xe7\xba\xbf\xe4\xb8\x8a\xe8\xbf\x90\xe8\xa1\x8c'), (3, b'\xe4\xb8\x8b\xe7\xba\xbf')])),
                ('remark', models.TextField(default=b'', verbose_name='\u5907\u6ce8')),
            ],
            options={
                'db_table': 'machineoperationsinfo',
                'verbose_name': '\u8bbe\u5907\u64cd\u4f5c\u8bb0\u5f55\u8868',
                'verbose_name_plural': '\u8bbe\u5907\u64cd\u4f5c\u8bb0\u5f55\u8868',
            },
        ),
    ]
