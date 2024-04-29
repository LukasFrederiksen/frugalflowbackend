from django.urls import path
from project.apps.users import views

urlpatterns = [
    path('', views.users, name='products'),
    path('<int:pk>', views.user_detail, name='user_by_id'),
    path('<int:userid>/cases', views.all_cases_for_a_user, name='get_all_cases_for_a_user'),
]
