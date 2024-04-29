from django.urls import path

from project.apps.manufacture import views


urlpatterns = [
    path('', views.manufactures, name='manufactures'),
    path('<int:id>/', views.manufacture, name='manufacture_by_id')
]
