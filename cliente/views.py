from django.shortcuts import render, redirect

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
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'login.html')