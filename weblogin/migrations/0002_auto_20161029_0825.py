# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblogin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailorder',
            old_name='dmain',
            new_name='dMain',
        ),
        migrations.RenameField(
            model_name='detailorder',
            old_name='dprice',
            new_name='dPrice',
        ),
        migrations.RenameField(
            model_name='productinfo',
            old_name='pclass',
            new_name='pClass',
        ),
        migrations.RenameField(
            model_name='sort',
            old_name='sclass',
            new_name='sClass',
        ),
    ]
