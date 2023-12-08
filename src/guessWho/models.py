from django.db import models

# Create your models here.
class CharacterSet(models.Model):
    CID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    AddDate = models.DateField(blank=True, null=True) 
    Guesses = models.IntegerField(blank=True, null=True) 
    RGuess = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.Name
    
class QuestionDB(models.Model):
    QID = models.IntegerField(primary_key=True) 
    QText = models.TextField()
    Added_On = models.DateField() 
    Last_Asked = models.DateField()
    
    def __str__(self):
        return self.QText
    def __unicode(self):
        return self.QID
    
class Attributevalue(models.Model):
    CID = models.ForeignKey(CharacterSet) 
    QID = models.ForeignKey(QuestionDB)
    Opvalue = models.IntegerField(blank=True,null=True)
    entropy = models.IntegerField(blank=True,null=True)

class questionLog(models.Model):
    GameID = models.IntegerField(primary_key=True)
    Qdata = models.TextField(blank=True,null=True)
    End = models.CharField(max_length=10)
