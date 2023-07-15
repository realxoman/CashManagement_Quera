from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns_api_v1 = [
    path('accounts/', include('accounts.urls'), name='accounts_api'),
    path('transactions/', include('transactions.urls'), name='transactions_api'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns_api_v1), name="api_urls"),
    path('schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
