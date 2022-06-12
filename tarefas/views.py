from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest, JsonResponse
from tarefas.models import CadastroDoacoes
import json


# Create your views here.
def paginaInicial(request):
    return render(request, 'index.html')
def about(request):
    return render(request, "About.html")

def cause(request):
    return render(request, "Cause.html")

def blog(request):
    return render(request, 'blog.html')

def doacoes(request):
    return render(request, "doacoes.html")

def pagInscritos(request):
    return render(request, 'account.html')

def contaCep(request):
    return render(request, 'accountCep.html')

def contato(request):
    return render(request, 'contact.html')

def enviaDadosDoacoes(request):
    cadastro = CadastroDoacoes()
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        #data = json.loads(request)
        roupas = request.GET['roupas']
        num_roupas = request.GET['num_roupas']
        objetos = request.GET['objetos']
        num_objetos = request.GET['num_objetos']
        calcados = request.GET['calcados']
        num_calcados = request.GET['num_calcados']
        brinquedos = request.GET['brinquedos']
        num_brinquedos = request.GET['num_brinquedos']

        retorno = cadastro.inserir_cadastro_doacoes(roupas, num_roupas, objetos, num_objetos, calcados, num_calcados, brinquedos, num_brinquedos)

        print("Entrouuu 2", roupas, num_roupas, objetos, num_objetos, calcados, num_calcados, brinquedos, num_brinquedos)
    return JsonResponse({'msg': retorno, 'status': 200}, status=200)