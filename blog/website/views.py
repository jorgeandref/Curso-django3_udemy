from django.shortcuts import render

def hello_blog(request):
    lista = ['django', 'python', 'git', 'linux', 'systemctl', 'html']
    name = {'nome': 'Eu sou sinistro, melhor que seu marido', 'lista_tecnologias': lista}
    return render(request, 'index.html', name, lista)