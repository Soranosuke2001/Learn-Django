from django.urls import path

from templates_app.views import other, relative

app_name = 'templates_app'

urlpatterns = [
  path("relative/", relative, name="relative"),
  path("other/", other, name="other"),
]
