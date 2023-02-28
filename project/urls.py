from django.urls import path
from . import views

urlpatterns = [
    path('allreadingmaterials/', views.members, name='members'),
    path('allreadingmaterials/details/<int:ID>', views.details, name='details')
]
