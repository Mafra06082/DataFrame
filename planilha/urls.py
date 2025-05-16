from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal_view, name='planilha'),
]