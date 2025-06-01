from django.urls import path
from . import views

urlpatterns = [
    path('send/<int:product_id>/', views.send_inquiry, name='send_inquiry'),
]