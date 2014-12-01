# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from __future__ import unicode_literals

from django.db import models

class Characterset(models.Model):
    cid = models.IntegerField(db_column='CID', primary_key=True, blank=True, null=False)
    name = models.TextField(db_column='Name')
    addDate = models.DateField(db_column='addDate', blank=True, null=True) 
    guesses = models.IntegerField(db_column='Guesses', blank=True, null=True) 
    rguess = models.IntegerField(db_column='RGuess', blank=True, null=True) 
    class Meta:
        managed = False
        db_table = 'CharacterSet'

class Questiondb(models.Model):
    qid = models.IntegerField(db_column='QID', primary_key=True, blank=True, null=False) 
    qtext = models.TextField(db_column='QText')
    freq = models.IntegerField(db_column='freq')
    addDate = models.DateField(db_column='addDate', blank=True, null=True) 
    lastasked = models.DateField(db_column='lastAsked', blank=True) 
    class Meta:
        managed = False
        db_table = 'questionDB'

class Attributevalue(models.Model):
    cs_id = models.IntegerField(db_column='CS_ID', blank=True, null=True) 
    q_id = models.IntegerField(db_column='Q_ID', blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'attributeValue'
        