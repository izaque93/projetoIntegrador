import email
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

def enviarEmailContatos(request):
    cadastro = CadastroDoacoes()
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        message = request.GET['message']
        name = request.GET['name']
        email = request.GET['email']
        subject = request.GET['subject']

        retorno = cadastro.enviar_email(message, name, email, subject)

        print("Entrouu enviar", retorno)

    return JsonResponse({'msg': "mensagem", 'status': 200}, status=200)

def cadastroComCep(request):
    cadastroComCep = CadastroDoacoes()
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        #data = json.loads(request)
        cep = request.GET['cep']
        rua = request.GET['rua']
        numero = request.GET['numero']
        complemento = request.GET['complemento']
        bairro = request.GET['bairro']
        cidade = request.GET['cidade']
        uf = request.GET['uf']
        email = request.GET['email']
        password = request.GET['password']
        confpassword = request.GET['confpassword']
        
        retorno = cadastroComCep.cadastroComCep(cep, rua, numero, complemento, bairro, cidade, uf, email, password, confpassword)
        print("Cadastrado ", cep, rua, numero, complemento, bairro, cidade, uf, email, password, confpassword)
        return JsonResponse({'msg': "mensagem", 'status': 200}, status=200)