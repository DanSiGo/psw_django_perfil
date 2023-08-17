from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conta
from django.contrib import messages
from django.contrib.messages import constants  # isso faz a chamada das mensagens que estão na constante MESSAGES_TAGS em settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    contas = Conta.objects.all()  # busca as contas no bd e atribui à variavel contas
    total_contas = 0
    for conta in contas:
        total_contas += conta.valor
    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas})

def cadastrar_banco(request):  # os dados no html vem na forma de dicionario, ex {'apelido':['valor'], etc}
    print(request.POST.get('icone'))
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')  # arquivos vem pelo método FILES e não POST

    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
        return redirect('/perfil/gerenciar/')

    conta = Conta(
        apelido = apelido,
        banco = banco,
        tipo = tipo,
        valor = valor,
        icone = icone
    )
    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso!')
    return redirect('/perfil/gerenciar/')

def deletar_banco(request, id):  # no html vai ser passado o id via tag django
    conta = Conta.objects.get(id=id)  # vamos individualizar a conta pelo id - dentro dos atributos da conta, buscar o id
    conta.delete()
    messages.add_message(request, constants.SUCCESS, 'Conta deletada com sucesso!')
    return redirect('/perfil/gerenciar')


