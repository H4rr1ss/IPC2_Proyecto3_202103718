from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('principal/', views.main, name="main"),
    path('lector/', views.xmlReader, name="leer"),
    path('consumo/', views.xmlConsumo, name="consumir"),
    path('cancelar/', views.cancelar, name="cancelar")
]
