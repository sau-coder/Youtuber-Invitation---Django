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