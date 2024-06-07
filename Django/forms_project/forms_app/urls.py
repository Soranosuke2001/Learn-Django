from django.urls import path

from forms_app.views import *

urlpatterns = [
  path("", index, name="index"),
  path("formpage/", form_name_view, name="form_name_view"),
]