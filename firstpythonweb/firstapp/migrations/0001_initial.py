# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookid', models.IntegerField()),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
