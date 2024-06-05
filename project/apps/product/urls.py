from django.urls import path
from project.apps.product import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:id>', views.product, name='product_by_id'),
    path('count', views.product_count, name='product_count'),
    path('is_unique/<int:is_unique>', views.products_is_unique, name='product_sorted_is_unique'),
]

