from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

from project.apps.users.views import CustomTokenObtainPairSerializer, CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/users/', include('project.apps.users.urls')),
    path('api/customers/', include('project.apps.customer.urls')),
    path('api/cases/', include('project.apps.case.urls')),
    path('api/vessels/', include('project.apps.vessel.urls')),
    path('api/manufactures/', include('project.apps.manufacture.urls')),
    path('api/products/', include('project.apps.product.urls')),
    #path('api/unique_products/', include('project.apps.unique_product.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
