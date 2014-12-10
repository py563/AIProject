# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guessWho', '0002_auto_20141208_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionlog',
            name='CurrQid',
        ),
        migrations.RemoveField(
            model_name='questionlog',
            name='NextQid',
        ),
        migrations.RemoveField(
            model_name='questionlog',
            name='OpVal',
        ),
        migrations.RemoveField(
            model_name='questionlog',
            name='StID',
        ),
        migrations.RemoveField(
            model_name='questionlog',
            name='StVal',
        ),
        migrations.AddField(
            model_name='questionlog',
            name='Qdata',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
