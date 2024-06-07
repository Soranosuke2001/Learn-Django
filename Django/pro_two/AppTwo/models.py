from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=264, unique=True)
  last_name = models.CharField(max_length=264, unique=True)
  email = models.CharField(max_length=264, unique=True)

  def __str__(self):
    return f'Name: {self.first_name} {self.last_name} | Email: {self.email}'
    