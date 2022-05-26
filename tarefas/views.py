from django.shortcuts import render, HttpResponse

# Create your views here.
def paginaInicial(request):
    return render(request, 'index.html')
def about(request):
    return render(request, "About.html")

def cause(request):
    return render(request, "Cause.html")

def branco(request):
    return render(request, 'branco.html')

def contato(request):
    return render(request, 'contact.html')
def account(request):
    return render(request, 'account.html')
