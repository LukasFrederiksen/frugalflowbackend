from django.urls import path
from project.apps.vessel import views

urlpatterns = [
    path('', views.vessels, name='vessels'),
    path('<int:id>', views.vessel, name='vessel_by_id'),
    path('count', views.vessel_count, name='vessel_count')
]
