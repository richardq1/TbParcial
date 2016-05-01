from django.conf.urls import url
from app_facebook import views

urlpatterns = [
    url(r'juego/',views.Home.as_view(),name='home' ),#se hace referenacia para que se vaya al home 
    url(r'Hola/',views.Prueba.as_view(),name='prueba' ),
    
]
from django.conf.urls import url
from app_facebook import views

urlpatterns = [
    url(r'juego/',views.Home.as_view(),name='home' ),#se hace referenacia para que se vaya al home 
    url(r'Hola/',views.Prueba.as_view(),name='prueba' ),
    
]
