from django.urls import path
from finances import views

urlpatterns = [
    path("", views.index, name="index"),
]