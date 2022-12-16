from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Youtuber(models.Model):
    crew_choices = (
        ('Solo' , 'Solo'),
        ('Small' , 'Small'),
        ('Large' , 'Large'),
    )

    camera_choices = (
        ('Canon' , 'Canon'),
        ('Nikon' , 'Nikon'),
        ('Sony' , 'Sony'),
        ('Red' , 'Red'),
        ('Fuji' , 'Fuji'),
        ('Panasonic' , 'Panasonic'),
        ('Other' , 'Other'),
    )

    category_choices= (
        ('Code' , 'Code'),
        ('Mobile_review' , 'Mobile_review'),
        ('Vlogs' , 'Vlogs'),
        ('Comedy' , 'Comedy'),
        ('Gaming' , 'Gaming'),
        ('Roasting' , 'Roasting'),
        ('Cooking' , 'Cooking'),
    )


    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to = 'media/ytuber/%Y/')
    video_url = models.CharField(max_length = 255)
    description = RichTextField()
    city = models.CharField(max_length = 255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices = crew_choices, max_length = 255)
    camera_type = models.CharField(choices = camera_choices , max_length = 255)
    subs_count = models.CharField(max_length = 255)
    category = models.CharField(choices = category_choices , max_length = 255)
    is_featured = models.BooleanField(default = False)
    created_date = models.DateTimeField(default = datetime.now , blank = True)

