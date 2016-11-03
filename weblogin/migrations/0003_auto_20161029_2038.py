# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblogin', '0002_auto_20161029_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uAddr',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe6\x94\xb6\xe8\xb4\xa7\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uPhone',
            field=models.DecimalField(null=True, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7', max_digits=11, decimal_places=0),
        ),
    ]
