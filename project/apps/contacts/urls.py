from django.urls import path
from project.apps.contacts import views


urlpatterns = [
    path('', views.contact_persons, name='contact_persons'),
]
