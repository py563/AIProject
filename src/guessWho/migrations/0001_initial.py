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
                ('value', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CharacterSet',
            fields=[
                ('CID', models.IntegerField(serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=30)),
                ('AddDate', models.DateField(null=True, blank=True)),
                ('Guesses', models.IntegerField(null=True, blank=True)),
                ('RGuess', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionDB',
            fields=[
                ('QID', models.IntegerField(serialize=False, primary_key=True)),
                ('QText', models.TextField()),
                ('Added_On', models.DateField()),
                ('Last_Asked', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='CID',
            field=models.ForeignKey(to='guessWho.CharacterSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='QID',
            field=models.ForeignKey(to='guessWho.QuestionDB'),
            preserve_default=True,
        ),
    ]
