"""Schemele URL pentru useri"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    #Pornim URL aurizatie ca defolt
    path('', include('django.contrib.auth.urls')),
    #Pagina de registrare
    path('register/', views.register, name='register')
]