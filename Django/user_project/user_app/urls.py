from django.urls import path
from user_app.views import register, user_login

app_name = 'user_app'

urlpatterns = [
  path("register/", register, name='register'),
  path("user_login/", user_login, name='user_login'),
]
