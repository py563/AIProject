# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guessWho', '0003_auto_20141210_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributevalue',
            name='CID',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='QID',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
