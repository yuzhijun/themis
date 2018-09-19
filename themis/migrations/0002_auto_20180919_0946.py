# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virtualserverinfo',
            name='vir_phy',
        ),
        migrations.AlterField(
            model_name='statisticsrecord',
            name='datatime',
            field=models.DateTimeField(default=b'2018-09-19', verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
