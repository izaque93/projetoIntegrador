from django.shortcuts import render, HttpResponse

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