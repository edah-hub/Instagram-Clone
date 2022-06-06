# User models

# Django
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.


class ProfileManager(models.Manager):
  def toggle_follow(self, request_user, username_to_toggle):
    profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
    user = request_user
    is_following = False
    if user in profile_.followers.all():
      profile_.followers.remove(user)
    else:
      profile_.followers.add(user)
      is_following = True
    return profile_, is_following

class Profile(models.Model):
    """
    Profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = CloudinaryField('image',blank=True,null=True)
    followers = models.ManyToManyField(User,related_name='is_following', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
     
        return self.user.username
