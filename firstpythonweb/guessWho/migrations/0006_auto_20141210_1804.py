# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guessWho', '0005_auto_20141210_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attrvalue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Opvalue', models.IntegerField(null=True, blank=True)),
                ('entropy', models.IntegerField(null=True, blank=True)),
                ('CID', models.ForeignKey(to='guessWho.CharacterSet')),
                ('QID', models.ForeignKey(to='guessWho.QuestionDB')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='attributevalue',
            name='CID',
        ),
        migrations.RemoveField(
            model_name='attributevalue',
            name='QID',
        ),
        migrations.DeleteModel(
            name='Attributevalue',
        ),
    ]
