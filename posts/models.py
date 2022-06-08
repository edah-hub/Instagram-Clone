from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse




class Image(models.Model):
  img_name = models.CharField(max_length=100, blank=True)
  image = CloudinaryField('image')
  caption = models.CharField(max_length=100, blank=True)
  likes = models.ManyToManyField(User, related_name='post_likes')
  user  = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def save_image(self):
    self.save()
    
  def delete_image(self):
    self.delete()  

  def __str__(self):
    return f'{self.user.username} Posted Images'

  def get_absolute_url(self):
    return reverse('image-post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
  content = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
  img_post = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='post_comments')
  created_at = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ['-created_at']
  
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
  
  @classmethod
  def get_comments(cls, pk):
    comments = cls.objects.filter(image=pk)
    return comments

  def __str__(self):
    return self.content

class Post(models.Model):
    """Post Model."""

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = CloudinaryField('image')
    # image = CloudinaryField('image')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return "{} by @{}".format(self.title, self.profile.user.username)
      
      
    def save_post(self):
      '''
      Method to save your post
      '''
      self.save()
      
      
    def delete_post(self):
        '''
        Method to delete your post
        '''
        self.delete()  



