# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cPrice', models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=4, decimal_places=2)),
                ('cNum', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='Detailorder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dNum', models.IntegerField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x95\xb0\xe9\x87\x8f')),
                ('dprice', models.IntegerField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x8d\x95\xe4\xbb\xb7')),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oSum', models.DecimalField(verbose_name=b'\xe6\x80\xbb\xe4\xbb\xb7', max_digits=4, decimal_places=2)),
                ('oTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x94\x9f\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4')),
                ('oIspay', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x94\xaf\xe4\xbb\x98')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pName', models.CharField(max_length=50, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('pPrice', models.DecimalField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x8d\x95\xe4\xbb\xb7', max_digits=4, decimal_places=2)),
                ('pStock', models.IntegerField(verbose_name=b'\xe5\xba\x93\xe5\xad\x98')),
                ('pDesc', models.CharField(max_length=1000, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\x8b\xe7\xbb\x8d')),
                ('pDetail', tinymce.models.HTMLField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe8\xaf\xa6\xe6\x83\x85')),
                ('pTime_data', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sclass', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uName', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('uPwd', models.CharField(max_length=100, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('uEmail', models.EmailField(max_length=254, verbose_name=b'\xe7\x94\xb5\xe5\xad\x90\xe9\x82\xae\xe4\xbb\xb6')),
                ('uPhone', models.DecimalField(verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7', max_digits=11, decimal_places=0)),
                ('uAddr', models.CharField(max_length=200, verbose_name=b'\xe6\x94\xb6\xe8\xb4\xa7\xe5\x9c\xb0\xe5\x9d\x80')),
                ('uTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='productinfo',
            name='pclass',
            field=models.ForeignKey(to='weblogin.Sort'),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='oUser',
            field=models.ForeignKey(to='weblogin.UserInfo'),
        ),
        migrations.AddField(
            model_name='detailorder',
            name='dProduct',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='weblogin.ProductInfo'),
        ),
        migrations.AddField(
            model_name='detailorder',
            name='dmain',
            field=models.ForeignKey(to='weblogin.OrderList'),
        ),
        migrations.AddField(
            model_name='charlist',
            name='cProduct',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='weblogin.ProductInfo'),
        ),
        migrations.AddField(
            model_name='charlist',
            name='cUser',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='weblogin.UserInfo'),
        ),
    ]
