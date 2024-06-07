from django.shortcuts import render
from django.http import HttpResponse

from AppTwo.models import *

# Create your views here.
def index(request):
  user_list = User.objects.order_by('first_name')
  users_dict = {
    'user_list': user_list
  }

  return render(request, 'AppTwo/index.html', context=users_dict)