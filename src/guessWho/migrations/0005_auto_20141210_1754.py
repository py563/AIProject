# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guessWho', '0004_auto_20141210_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributevalue',
            name='CID',
            field=models.ForeignKey(to='guessWho.CharacterSet'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='QID',
            field=models.ForeignKey(to='guessWho.QuestionDB'),
            preserve_default=True,
        ),
    ]
