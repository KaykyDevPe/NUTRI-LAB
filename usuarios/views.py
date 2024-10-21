from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')
        
    
    return render(request, 'cadastro.html')

def logar(request):
    pass
