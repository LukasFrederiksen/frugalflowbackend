from django.urls import path

from project.apps.customer import views

urlpatterns = [
    path('', views.customers, name='customers'),
    path('<int:id>/', views.customer, name='customer_by_id'),
    path('count', views.customer_count, name='customer_count')
    ]
