from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Image(models.Model):
    img_name = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image')
