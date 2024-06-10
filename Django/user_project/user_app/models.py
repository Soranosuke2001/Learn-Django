from django.db import models

from django.contrib.auth.models import User

# Create your models here.
# Note: name the class UserProfileInfoForm

class UserProfileInfo(models.Model):
  # Note: This extends the class basically.
  #   The `User` class already comes with Username, FirstName, Password, Surname and Email
  #   In order to add more attributes, we need to extend the class by the using the code below
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  portfolio_site = models.URLField(blank=True)
  profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

  def __str__(self):
    return self.user.username
  
