from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from .utils import password_is_valid, email_is_valid, username_is_valid
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')
        elif not email_is_valid(request, email):
            return redirect('/auth/cadastro')
        elif not username_is_valid(request, username):
            return redirect('/auth/cadastro')
              
        try:
            user= User.objects.create_user(username=username,
                                           password=senha,
                                           email=email,
                                           is_active=False)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso, necessário solicitar a ativação.')
            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.WARNING, 'Erro interno do sistema.')
            return redirect('/auth/cadastro')
        
    return render(request, 'cadastro.html')

def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)
        
        if not usuario:
            messages.add_message(request, constants.WARNING, 'Usuário ou senha inválido')
            return redirect('/auth/cadastro')
        else:
            auth.login(request, usuario)
            return redirect('/')
    
        