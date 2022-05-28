from tarefas import views
from django.urls import path

urlpatterns = [
    path('', views.paginaInicial, name = 'index'),
    path('ajuda', views.about, name = 'About'),
    path('causa', views.cause, name = 'Cause'),
    path('blog', views.blog, name ='blog'),
    path('doacoes', views.doacoes, name = 'doacoes'),
    path('entrar', views.pagInscritos, name = 'account'),
    path('cep', views.contaCep, name = 'accountCep')
]
