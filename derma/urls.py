from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('bla', views.make_booking)
]