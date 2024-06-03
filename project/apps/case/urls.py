from django.urls import path

from project.apps.case import views

urlpatterns = [
    path('', views.cases, name='cases'),
    path('<int:id>', views.case, name='case_by_id'),
    path('count', views.case_count, name='case_count'),
    path('addproduct', views.add_product, name='add_product_to_case')
    ]
