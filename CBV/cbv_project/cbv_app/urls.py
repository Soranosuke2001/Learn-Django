from django.urls import path

from cbv_app.views import *

app_name = 'cbv_app'

urlpatterns = [
  path("", SchoolListView.as_view(), name="list"),
  path("<int:pk>/", SchoolDetailView.as_view(), name="detail"),
  path("create/", SchoolCreateView.as_view(), name="create"),
  path("update/<int:pk>/", SchoolUpdateView.as_view(), name="update"),
  path("delete/<int:pk>/", SchoolDeleteView.as_view(), name="delete"),
]
