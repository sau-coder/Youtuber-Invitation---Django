from django.db import models

# Create your models here.

class Slider(models.Model):
    head_line = models.CharField(max_length = 255)
    sub_title = models.CharField(max_length = 255)
    button_text = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to = 'media/slider/%Y/')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.head_line

class Team(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    role = models.CharField(max_length = 100)
    fb_link = models.CharField(max_length = 255)
    insta_link = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to = "media/team/%Y/")
    created_at =  models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.first_name

