from django.urls import path
from project.apps.product import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:id>', views.product, name='product_by_id'),
    path('count', views.product_count, name='product_count'),
    path('create_unique_product/', views.product_create, name='create_unique_product'),
    path('unique_product/<int:id>', views.unique_product, name='unique_product_by_id'),
    path('unique_products/', views.unique_products, name='unique_products')
]

