# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblogin', '0004_rencentmap'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cPrice', models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=4, decimal_places=2)),
                ('cNum', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
            ],
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='cProduct',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='cUser',
        ),
        migrations.RenameField(
            model_name='productinfo',
            old_name='pTime_data',
            new_name='pTime',
        ),
        migrations.AddField(
            model_name='productinfo',
            name='pImg',
            field=models.ImageField(default='', upload_to=b'upload/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinfo',
            name='pUnit',
            field=models.CharField(default='', max_length=20, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CharList',
        ),
        migrations.AddField(
            model_name='cartlist',
            name='cProduct',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='weblogin.ProductInfo'),
        ),
        migrations.AddField(
            model_name='cartlist',
            name='cUser',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='weblogin.UserInfo'),
        ),
    ]
