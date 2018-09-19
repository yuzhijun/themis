# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themis', '0002_auto_20180919_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualserverinfo',
            name='vir_phy',
            field=models.ForeignKey(default=1, to='themis.PhysicalServerInfo'),
            preserve_default=False,
        ),
    ]
