from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
  return render(request, 'forms_app/index.html')


def form_name_view(request):
  form = forms.FormName()

  if request.method == 'POST':
    form = forms.FormName(request.POST)

    if form.is_valid():
      print(f"Validation Success!")
      
      print(f"Name: {form.cleaned_data['name']}")
      print(f"Email: {form.cleaned_data['email']}")
      print(f"Text: {form.cleaned_data['text']}")

  return render(request, 'forms_app/forms_page.html', context={ 'form': form })
