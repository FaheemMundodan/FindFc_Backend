from django.db import models



class Event(models.Model):
    
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    image = models.ImageField(upload_to='events/', default='path/to/placeholder/image.jpg')
    date = models.DateField(default='2002-04-01')  # Correct default value format
    title= models.CharField(max_length=100,default="")

class StudyMaterial(models.Model):
    category = models.CharField(max_length=2)  # UG or PG
    year = models.IntegerField()
    material_type = models.CharField(max_length=50)  # Notes, Previous Year Papers, etc.
    file = models.FileField(upload_to='study_materials/')

