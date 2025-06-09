from django.urls import path
from products import views
from .views import product_list, product_detail, product_create, product_update, product_delete, category_view


app_name = 'products'

urlpatterns = [
    path('', product_list, name='products_list'),  # <-- 이 줄에서 name='products_list'인지 확인
    path('create/', product_create, name='product_create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/delete/', product_delete, name='product_delete'),
    path('<int:pk>/update/', product_update, name='product_update'),
    path('category/<str:category_name>/', category_view, name='category_view'),
]