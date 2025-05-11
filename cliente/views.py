from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        # aqui você pode colocar validação simples só para testar
        if usuario == "admin" and senha == "123":
            return redirect('/planilha/')
        elif usuario == "" and senha == "":
            return redirect('/planilha/')
        else:
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'login.html')