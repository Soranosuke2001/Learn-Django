from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  my_dict = {
    'title': 'Help Page',
    'help_num': 'Please call 123-1234-1234 for more support.'
  }

  return render(request, 'AppTwo/help.html', context=my_dict)