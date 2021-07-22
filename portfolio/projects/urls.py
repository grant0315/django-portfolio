from django.urls import path
from . import views

# The <int:pk> notation is used to dynamically generate primary keys (/1, /2, etc...) 
# This just tells Django that the value passed in the URL is an integer, and its variable name is pk
urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]