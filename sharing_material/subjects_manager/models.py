from django.db import models

# Create your models here.


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    IdAd = models.CharField(max_length=200)
    Date = models.DateTimeField()
    School = models.CharField(max_length=200)
