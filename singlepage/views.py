from django.http import JsonResponse, Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from website.models import Jogador

bdJogadores = [
    {
        "nome": "Ronaldo",
        "apelido": "Aveiro",
        "clube": "Juventus",
        "autor": "Antonio",
        "bio": "Cristiano Ronaldo dos Santos Aveiro(Funchal, 5 de fevereiro de 1985) é um futebolista português que atua como extremo-esquerdo ou ponta de lança. Atualmente joga pela Juventus e pela Seleção Portuguesa."
    },
    {
        "nome": "Lionel",
        "apelido": "Messi",
        "clube": "Barcelona",
        "autor": "Antonio"
    },
    {
        "nome": "Joao",
        "apelido": "Palhinha",
        "clube": "Sporting",
        "autor": "Antonio"
    },
    {
        "nome": "Pedro",
        "apelido": "Gonçalves",
        "clube": "Sporting",
        "autor": "Antonio"
    },
    {
        "nome": "Sergio",
        "apelido": "Oliveira",
        "clube": "Porto",
        "autor": "Antonio"
    },
    {
        "nome": "Mehdi",
        "apelido": "Taremi",
        "clube": "Porto",
        "autor": "Antonio"
    },
    {
        "nome": "Julien",
        "apelido": "Weigl",
        "clube": "Benfica",
        "autor": "Antonio"
    },
    {
        "nome": "Lucas",
        "apelido": "Verissimo",
        "clube": "Benfica",
        "autor": "Antonio"
    },
    {
        "nome": "Joao",
        "apelido": "Novais",
        "clube": "Braga",
        "autor": "Antonio"
    },
    {
        "nome": "Lucas",
        "apelido": "Piazon",
        "clube": "Braga",
        "autor": "Antonio"
    }
]


def index_page_view(request):
    context = {'jogadores': Jogador.objects.all()}
    return render(request, 'singlepage/index.html', context)


def section(request, num):
    if num == 1:
        return JsonResponse({"jogadores": bdJogadores})
    if num == 2:
        return HttpResponse(bdJogadores)
    else:
        raise Http404("No such section")


# Create your views here.
