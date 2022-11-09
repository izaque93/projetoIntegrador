from tarefas import views
from django.urls import path

urlpatterns = [
    path('', views.paginaInicial, name = 'index'),
    path('cadastro', views.about, name = 'cadastro'),
    path('causa', views.cause, name = 'Cause'),
    path('blog', views.blog, name ='blog'),
    path('doacoes', views.doacoes, name = 'doacoes'),
    path('entrar', views.entrar, name = 'entrar'),
    #path('entrar', views.pagInscritos, name = 'entrar'),
    path('cep', views.contaCep, name = 'accountCep'),
    path('contato', views.contato, name= 'contact'),
    path('enviaDadosDoacoes', views.enviaDadosDoacoes, name='enviaDadosDoacoes'),
    path('enviarEmailContatos', views.enviarEmailContatos, name='enviarEmailContatos'),
    path('cadastroComCep', views.cadastroComCep, name = 'cadastroComCep'),
    path('entrarIndex', views.entrarIndex, name = 'entrarIndex'),
]
