from django.urls import path
from project.apps.unique_product import views

urlpatterns = [
    path('', views.unique_products, name='unique_products')
]

