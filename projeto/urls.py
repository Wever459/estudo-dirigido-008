"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
from .views import (
    UnidadeListCreate, 
    SalaListCreate, 
    StatusListCreate, 
    BemListCreate, 
    BemDetail
)

urlpatterns = [
    path("unidades/", UnidadeListCreate.as_view()),
    path("salas/", SalaListCreate.as_view()),
    path("status/", StatusListCreate.as_view()),
    path("bens/", BemListCreate.as_view()),
    path("bens/<int:pk>/", BemDetail.as_view()),
    

]