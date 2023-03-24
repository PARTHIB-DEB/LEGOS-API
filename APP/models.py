from django.db import models

# Create your models here.
class legos(models.Model):
    comics=models.TextField()
    names=models.CharField(max_length=5000)
    total=models.IntegerField()
    seller=models.TextField()