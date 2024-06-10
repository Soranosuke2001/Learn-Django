from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.http import HttpResponse

from cbv_app.models import *


# Create your views here.

# This is a function based view
# def index(request):
#   return render(request, 'index.html')


# This is a class based view (Example)
# class CBView(View):
#   def get(self, request):
#     return HttpResponse('CLASS BASED VIEWS ARE COOL!')


# This is a class based view with template views
class IndexView(TemplateView):
  template_name = 'index.html'

  # This method is required in order to use context
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['injectme'] = 'BASIC INJECTION!'

    return context
  

class SchoolListView(ListView):
  model = School
  context_object_name = 'schools'


class SchoolDetailView(DetailView):
  model = School
  context_object_name = 'school_detail'
  template_name = 'cbv_app/school_detail.html'
  

class SchoolCreateView(CreateView):
  model = School
  fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
  model = School
  fields = ('name', 'principal')


class SchoolDeleteView(DeleteView):
  model = School
  success_url = reverse_lazy('cbv_app:list')

