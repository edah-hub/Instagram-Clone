from django.db import models
from cloudinary.models import CloudinaryField
from accounts.models import Profile

# Create your models here.

class Image(models.Model):
    img_name = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image')


class Post(models.Model):
    """Post Model."""

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    image = CloudinaryField('image')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return "{} by @{}".format(self.title, self.profile.user.username)
