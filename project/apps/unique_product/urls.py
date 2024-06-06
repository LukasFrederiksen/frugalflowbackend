from django.urls import path
from project.apps.unique_product import views

urlpatterns = [
    path('', views.unique_products, name='unique_products'),
    path('<int:id>', views.unique_product, name='unique_products'),
    path('status_payment_enums', views.status_payment_enums, name='unique_products_enums'),
    path('status_shipping_enums', views.status_shipping_enums, name='unique_products_enums'),
]
