# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributevalue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cs_id', models.IntegerField(null=True, db_column='CS_ID', blank=True)),
                ('q_id', models.IntegerField(null=True, db_column='Q_ID', blank=True)),
                ('value', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'attributeValue',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Characterset',
            fields=[
                ('cid', models.IntegerField(serialize=False, primary_key=True, db_column='CID', blank=True)),
                ('name', models.TextField(db_column='Name')),
                ('addDate', models.DateField(null=True, db_column='addDate', blank=True)),
                ('guesses', models.IntegerField(null=True, db_column='Guesses', blank=True)),
                ('rguess', models.IntegerField(null=True, db_column='RGuess', blank=True)),
            ],
            options={
                'db_table': 'CharacterSet',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questiondb',
            fields=[
                ('qid', models.IntegerField(serialize=False, primary_key=True, db_column='QID', blank=True)),
                ('qtext', models.TextField(db_column='QText')),
                ('freq', models.IntegerField(db_column='freq')),
                ('addDate', models.DateField(null=True, db_column='addDate', blank=True)),
                ('lastasked', models.DateField(db_column='lastAsked', blank=True)),
            ],
            options={
                'db_table': 'questionDB',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
