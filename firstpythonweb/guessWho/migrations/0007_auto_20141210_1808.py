# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guessWho', '0006_auto_20141210_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjOptions',
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
            model_name='attrvalue',
            name='CID',
        ),
        migrations.RemoveField(
            model_name='attrvalue',
            name='QID',
        ),
        migrations.DeleteModel(
            name='Attrvalue',
        ),
    ]
