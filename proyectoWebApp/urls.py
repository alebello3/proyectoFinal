from django.contrib import admin
from django.urls import path
from proyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',views.home, name="home"),
    path('nosotros',views.nosotros, name="nosotros"),
    path('tienda',views.tienda, name="tienda"),
    
    
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)