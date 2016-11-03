# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblogin', '0003_auto_20161029_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='RencentMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rTime', models.DateTimeField(auto_now_add=True)),
                ('rProName', models.ForeignKey(to='weblogin.ProductInfo')),
                ('rUser', models.ForeignKey(to='weblogin.UserInfo')),
            ],
        ),
    ]
