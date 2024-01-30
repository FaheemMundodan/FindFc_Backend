from django.db import models

# Create your models here.
class details (models.Model):
    time= models.IntegerField()
    venue= models.CharField(max_length=64)
    poster=models.FileField(default="")

def __str__(self):
    return f"{self.id} - {self.time} For {self.venue}"

