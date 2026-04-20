from django.urls import path
from finances import views

urlpatterns = [
    path("", views.index, name="index"),
    path("transaction/<int:transaction_id>/", views.transaction, name="transaction"),
]