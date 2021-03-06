# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CabinetInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cab_name', models.CharField(max_length=10, verbose_name='\u673a\u67dc\u7f16\u53f7')),
                ('cab_lever', models.CharField(max_length=2, verbose_name='\u673a\u5668U\u6570,1-10\u5206\u522b\u4ee3\u88681~10\u5c42')),
            ],
            options={
                'db_table': 'cabinetinfo',
                'verbose_name': '\u673a\u67dc\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u673a\u67dc\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='ConnectionInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ssh_username', models.CharField(default=b'', max_length=10, null=True, verbose_name='ssh\u7528\u6237\u540d')),
                ('ssh_userpasswd', models.CharField(default=b'', max_length=40, null=True, verbose_name='ssh\u7528\u6237\u5bc6\u7801')),
                ('ssh_hostip', models.CharField(default=b'', max_length=40, null=True, verbose_name='ssh\u767b\u5f55\u7684ip')),
                ('ssh_host_port', models.CharField(default=b'', max_length=10, null=True, verbose_name='ssh\u767b\u5f55\u7684\u7aef\u53e3')),
                ('ssh_rsa', models.CharField(default=b'', max_length=64, verbose_name='ssh\u79c1\u94a5')),
                ('rsa_pass', models.CharField(default=b'', max_length=64, verbose_name='\u79c1\u94a5\u7684\u5bc6\u94a5')),
                ('ssh_status', models.IntegerField(default=0, verbose_name='\u7528\u6237\u8fde\u63a5\u72b6\u6001,0-\u767b\u5f55\u5931\u8d25,1-\u767b\u5f55\u6210\u529f')),
                ('ssh_type', models.IntegerField(default=0, verbose_name='\u7528\u6237\u8fde\u63a5\u7c7b\u578b, 1-rsa\u767b\u5f55,2-dsa\u767b\u5f55,3-ssh_rsa\u767b\u5f55,4-docker\u6210\u529f,5-docker\u65e0\u6cd5\u767b\u5f55')),
                ('sn_key', models.CharField(default=b'', max_length=256, verbose_name='\u552f\u4e00\u8bbe\u5907ID')),
            ],
            options={
                'db_table': 'connectioninfo',
                'verbose_name': '\u7528\u6237\u767b\u5f55\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u7528\u6237\u767b\u5f55\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='NetConnectionInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel_username', models.CharField(default=b'', max_length=10, null=True, verbose_name='\u7528\u6237\u540d')),
                ('tel_userpasswd', models.CharField(default=b'', max_length=40, null=True, verbose_name='\u8bbe\u5907\u7528\u6237\u5bc6\u7801')),
                ('tel_enpasswd', models.CharField(default=b'', max_length=40, null=True, verbose_name='\u8bbe\u5907\u8d85\u7ea7\u7528\u6237\u5bc6\u7801')),
                ('tel_host_port', models.CharField(default=b'', max_length=10, null=True, verbose_name='\u8bbe\u5907\u767b\u5f55\u7684\u7aef\u53e3')),
                ('tel_hostip', models.CharField(default=b'', max_length=40, null=True, verbose_name='\u8bbe\u5907\u767b\u5f55\u7684ip')),
                ('tel_status', models.IntegerField(default=0, verbose_name='\u7528\u6237\u8fde\u63a5\u72b6\u6001,0-\u767b\u5f55\u5931\u8d25,1-\u767b\u5f55\u6210\u529f')),
                ('tel_type', models.IntegerField(default=0, verbose_name='\u7528\u6237\u8fde\u63a5\u7c7b\u578b, 1-\u666e\u901a\u7528\u6237\u53ef\u767b\u5f55,2-\u8d85\u7ea7\u7528\u6237\u53ef\u767b\u5f55')),
                ('sn_key', models.CharField(default=b'', max_length=256, verbose_name='\u552f\u4e00\u8bbe\u5907ID')),
            ],
            options={
                'db_table': 'netconnectioninfo',
                'verbose_name': '\u7f51\u7edc\u8bbe\u5907\u7528\u6237\u767b\u5f55\u4fe1\u606f',
                'verbose_name_plural': '\u7f51\u7edc\u8bbe\u5907\u7528\u6237\u767b\u5f55\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='NetWorkInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_ip', models.CharField(max_length=40, verbose_name='\u7f51\u7edc\u8bbe\u5907ip')),
                ('host_name', models.CharField(max_length=10, verbose_name='\u7f51\u7edc\u8bbe\u5907\u540d')),
                ('sn', models.CharField(default=b'', max_length=256, verbose_name='SN\uff0d\u8bbe\u5907\u7684\u552f\u4e00\u6807\u8bc6')),
                ('net_cab', models.ForeignKey(to='themis.CabinetInfo')),
            ],
            options={
                'db_table': 'networkinfo',
                'verbose_name': '\u7f51\u7edc\u8bbe\u5907\u8868',
                'verbose_name_plural': '\u7f51\u7edc\u8bbe\u5907\u8868',
            },
        ),
        migrations.CreateModel(
            name='OtherMachineInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=40, verbose_name='\u8bbe\u5907ip')),
                ('sn_key', models.CharField(max_length=256, verbose_name='\u8bbe\u5907\u7684\u552f\u4e00\u6807\u8bc6')),
                ('machine_name', models.CharField(max_length=20, verbose_name='\u8bbe\u5907\u540d\u79f0')),
                ('remark', models.TextField(default=b'', verbose_name='\u5907\u6ce8')),
                ('reson_str', models.CharField(default=b'', max_length=128, verbose_name='\u5f52\u7eb3\u539f\u56e0')),
                ('oth_cab', models.ForeignKey(to='themis.CabinetInfo')),
            ],
            options={
                'db_table': 'othermachineinfo',
                'verbose_name': '\u5176\u5b83\u8bbe\u5907\u8868',
                'verbose_name_plural': '\u5176\u5b83\u8bbe\u5907\u8868',
            },
        ),
        migrations.CreateModel(
            name='PhysicalServerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_ip', models.CharField(max_length=40, verbose_name='\u670d\u52a1\u5668IP')),
                ('machine_brand', models.CharField(default=b'--', max_length=60, verbose_name='\u670d\u52a1\u5668\u54c1\u724c')),
                ('system_ver', models.CharField(default=b'', max_length=30, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c')),
                ('sys_hostname', models.CharField(max_length=15, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u4e3b\u673a\u540d')),
                ('mac', models.CharField(default=b'', max_length=512, verbose_name='MAC\u5730\u5740')),
                ('sn', models.CharField(default=b'', max_length=256, verbose_name='SN-\u4e3b\u673a\u7684\u552f\u4e00\u6807\u8bc6')),
                ('vir_type', models.CharField(default=b'', max_length=2, verbose_name='\u5bbf\u4e3b\u673a\u7c7b\u578b')),
                ('conn_phy', models.ForeignKey(to='themis.ConnectionInfo')),
                ('ser_cabin', models.ForeignKey(to='themis.CabinetInfo')),
            ],
            options={
                'db_table': 'physicalserverinfo',
                'verbose_name': '\u7269\u7406\u670d\u52a1\u5668\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u7269\u7406\u670d\u52a1\u5668\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='StatisticsRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datatime', models.DateTimeField(default=b'2018-09-17', verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('all_count', models.IntegerField(default=0, verbose_name='\u6240\u6709\u8bbe\u5907\u6570\u91cf')),
                ('pyh_count', models.IntegerField(default=0, verbose_name='\u7269\u7406\u8bbe\u5907\u6570\u91cf')),
                ('net_count', models.IntegerField(default=0, verbose_name='\u7f51\u7edc\u8bbe\u5907\u6570\u91cf')),
                ('other_count', models.IntegerField(default=0, verbose_name='\u5176\u4ed6\u8bbe\u5907\u6570\u91cf')),
                ('kvm_count', models.IntegerField(default=0, verbose_name='KVM\u8bbe\u5907\u6570\u91cf')),
                ('docker_count', models.IntegerField(default=0, verbose_name='Docker\u8bbe\u5907\u6570\u91cf')),
                ('vmx_count', models.IntegerField(default=0, verbose_name='VMX\u8bbe\u5907\u6570\u91cf')),
            ],
            options={
                'db_table': 'statisticsrecord',
                'verbose_name': '\u626b\u63cf\u540e\u7684\u6c47\u603b\u786c\u4ef6\u7edf\u8ba1\u4fe1\u606f',
                'verbose_name_plural': '\u626b\u63cf\u540e\u7684\u6c47\u603b\u786c\u4ef6\u7edf\u8ba1\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='VirtualServerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_ip', models.CharField(max_length=40, verbose_name='\u670d\u52a1\u5668IP')),
                ('server_type', models.CharField(default=b'', max_length=80, verbose_name='\u670d\u52a1\u5668\u7c7b\u578b:kvm,Vmware,Docker,others')),
                ('system_ver', models.CharField(default=b'', max_length=30, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c')),
                ('sys_hostname', models.CharField(max_length=15, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u4e3b\u673a\u540d')),
                ('mac', models.CharField(default=b'', max_length=512, verbose_name='MAC\u5730\u5740')),
                ('sn', models.CharField(default=b'', max_length=256, verbose_name='SN-\u4e3b\u673a\u7684\u552f\u4e00\u6807\u8bc6')),
                ('conn_vir', models.ForeignKey(to='themis.ConnectionInfo')),
                ('vir_phy', models.ForeignKey(to='themis.PhysicalServerInfo')),
            ],
            options={
                'db_table': 'virtualserverinfo',
                'verbose_name': '\u865a\u62df\u8bbe\u5907\u8868',
                'verbose_name_plural': '\u865a\u62df\u8bbe\u5907\u8868',
            },
        ),
        migrations.AddField(
            model_name='netconnectioninfo',
            name='dev_info',
            field=models.ForeignKey(to='themis.NetWorkInfo'),
        ),
    ]
