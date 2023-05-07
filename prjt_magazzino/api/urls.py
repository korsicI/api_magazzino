from django.urls import path
from . import views

urlpatterns = [
    path('scatole/', views.scatola_list, name='scatola_list'),
    path('scatole/<int:pk>/', views.scatola_detaglio, name='scatola_detaglio'),
    path('unita/', views.unita_list, name='unita_list'),
    path('unita/<int:pk>/', views.unita_detaglio, name='unita_detaglio'),
]