"""
URL configuration for HEMATOCARE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ponto_de_coleta/', views.ponto_de_coleta_list, name='ponto_de_coleta_list'),
    path('ponto_de_coleta/<str:cnpj>/', views.ponto_de_coleta_detail, name='ponto_de_coleta_detail'),
    path('ponto_de_coleta/create/', views.ponto_de_coleta_create, name='ponto_de_coleta_create'),
    path('ponto_de_coleta/update/<str:cnpj>/', views.ponto_de_coleta_update, name='ponto_de_coleta_update'),
    path('ponto_de_coleta/delete/<str:cnpj>/', views.ponto_de_coleta_delete, name='ponto_de_coleta_delete'),
    # Defina as URLs para as outras tabelas...
]
