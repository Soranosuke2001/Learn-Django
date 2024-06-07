import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro_two.settings')

import django
django.setup()

import random
from faker import Faker

from AppTwo.models import *

fakegen = Faker()

def populate(n=5):
  for _ in range(n):
    fake_name = fakegen.name().split(" ")
    fake_first_name = fake_name[0]
    fake_last_name = fake_name[1]
    fake_email = fakegen.email()

    user_info = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
    user_info.save()



if __name__ == "__main__":
  print("Populate Script is now running!")
  populate()
  print("Successfully generated fake data")
