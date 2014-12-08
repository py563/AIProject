# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guessWho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='questionLog',
            fields=[
                ('GameID', models.IntegerField(serialize=False, primary_key=True)),
                ('StVal', models.IntegerField()),
                ('CurrQid', models.IntegerField()),
                ('OpVal', models.IntegerField()),
                ('NextQid', models.IntegerField()),
                ('End', models.CharField(max_length=10)),
                ('StID', models.ForeignKey(to='guessWho.QuestionDB')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='attributevalue',
            old_name='value',
            new_name='Opvalue',
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='entropy',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
