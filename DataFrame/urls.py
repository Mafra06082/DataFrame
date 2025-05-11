from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cliente.urls')),     # login
    path('planilha/', include('planilha.urls')),  # upload e merge
]