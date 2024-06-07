from django.shortcuts import render

from AppTwo.forms import NewUserForm


# Create your views here.
def index(request):
  return render(request, 'AppTwo/index.html')


def users_view(request):
  form = NewUserForm()

  if request.method == "POST":
    form = NewUserForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      
      # This will take you back to the home page
      return index(request)
    
    print("ERROR FORM INVALID")

  return render(request, 'AppTwo/users.html', context={ 'form': form })
  