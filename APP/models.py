from django.db import models

# Create your models here.
class legos(models.Model):
    comics=models.TextField()
    names=models.CharField(max_length=5000)
    total=models.IntegerField(default=0)
    seller=models.TextField()
    
    def __str__(self):
        return self.comics