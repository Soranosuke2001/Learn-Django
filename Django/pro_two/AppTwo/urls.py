from django.urls import path

from AppTwo import views

urlpatterns = [
  path("", views.index, name="index"),
  path("users/", views.users_view, name="users_view")
]
