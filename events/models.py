from django.db import models
from django import forms

# Create your models here.
class details (models.Model):
    time= models.IntegerField()
    venue= models.CharField(max_length=64)
    poster=models.FileField(default="")



#     CATEGORY = [
#         ('1', 'UG'),
#         ('2', 'PG'),
#     ]

#     YEAR = [
#         ('1', 'First Year'),
#         ('2', 'Second Year'),
#         ('3', 'Third Year'),
#     ]
#     MATERIAL_TYPE = [
#         ('1', 'First Year'),
#         ('2', 'Second Year'),
#         ('3', 'Third Year'),
#     ]

#     single_option1 =  ArrayField(
#         models.CharField(max_length=10, choices=CATEGORY),
#         size=3,)
#     single_option2 = forms.ChoiceField(choices=YEAR)
#     single_option1 = forms.ChoiceField(choices=MATERIAL_TYPE)

# def __str__(self):
#     return f"{self.id} - {self.time} For {self.venue}"




# Your main model
# class MyModel(models.Model):
    # name = models.CharField(max_length=100, default="50")
    # course = models.ForeignKey(Course, related_name='my_models', on_delete=models.CASCADE, default= "50")
    # Year = models.ForeignKey(Year, related_name='my_models', on_delete=models.CASCADE, default= "0")
    # def __str__(self):
    #     return self.name
class Material(models.Model):
    # Define choices for the course field
    COURSE_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]

    # Define choices for the year field
    YEAR_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ]

    TYPE_CHOICES = [
        ('Notes', 'Notes'),
        ('PYQ', 'Previous Year Questions'),
    ]

    # File upload field
    file = models.FileField(upload_to='materials/')  # Adjust the upload_to path as needed

    # Single select field for course
    course = models.CharField(
        max_length=2,
        choices=COURSE_CHOICES,
        default='UG',  # Set default value if desired
    )

    # Single select field for year
    year = models.CharField(
        max_length=1,
        choices=YEAR_CHOICES,
        default='1',  # Set default value if desired
    )
    material_type=models.CharField(
        max_length=25,
        choices=TYPE_CHOICES,
        default="Notes"
    )

    def __str__(self):
        return f"{self.course} Year {self.year} Material"
    


# Your main model

