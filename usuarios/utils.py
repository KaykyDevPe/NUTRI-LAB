import re
from django.contrib import messages
from django.contrib.messages import constants

def password_is_valid(request, password, confirm_password):
    
    if len(password) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha a senha')
        
    if len(password) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        return False

    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    
    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
        return False

    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
        return False

    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False

    return True

def username_is_valid(request, username):
    
    if len(username) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha o usuário')
        return False
    
    return True

def email_is_valid(request, email):
    if len(email) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha o email')
        return False
    
    return True