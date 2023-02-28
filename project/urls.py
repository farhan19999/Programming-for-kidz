from django.urls import path
from . import views

urlpatterns = [
    path('allreadingmaterials/', views.members, name='members'),
    path('allreadingmaterials/details/<int:ID>', views.details, name='details'),
    path('mcq/<int:c_id>/<int:q_id>',views.mcq, name='mcq')
    
]
