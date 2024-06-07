import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from faker import Faker

from first_app.models import *

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
  t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
  t.save()

  return t


def populate(n=5):
  for _ in range(n):
    top = add_topic()

    fake_url = fakegen.url()
    fake_date = fakegen.date()
    fake_name = fakegen.company()

    page = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

    record = AccessRecord.objects.get_or_create(name=page, date=fake_date)[0]


if __name__ == "__main__":
  print("Populate Script is now running!")
  populate()
  print("Successfully generated fake data")
