from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    # Renders
    path('', views.Facturas.as_view(), name="Facturas"),

     
]
