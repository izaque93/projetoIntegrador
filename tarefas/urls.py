from tarefas import views
from django.urls import path

urlpatterns = [
    path('', views.paginaInicial, name = 'index'),
    path('About/', views.about, name = 'About'),
    path('Cause/', views.cause, name = 'Cause'),
    path('branco/', views.branco, name ='branco')
]
