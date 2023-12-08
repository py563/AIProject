from django.db import models

# Create your models here.
class books(models.Model):
    bookid=models.IntegerField()
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=45)
