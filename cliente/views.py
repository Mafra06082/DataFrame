from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # validação

        if usuario == "admin" and senha == "123":
            return redirect('/planilha/')
        elif usuario == "otavio" and senha == "981104425":
            return redirect('/planilha/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário incorreto.')
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'login.html')