from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.current_time, name='current_time'),
    path('name/', views.name_db, name = 'name_db'),
]