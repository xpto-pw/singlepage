from django.http import HttpResponseRedirect, JsonResponse, Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from website.forms import ContactoForm, QuizzForm, ComentarioForm, JogadorForm
from website.models import Contacto, Comentario, Jogador


def index_page_view(request):
    return render(request, 'website/index.html')


def equipas_page_view(request):
    return render(request, 'website/equipas.html')


def jogadores_page_view(request):
    return render(request, 'website/jogadores.html')


def contactos_page_view(request):
    context = {'contactos': Contacto.objects.all()}
    return render(request, 'website/contactos.html', context)


def contactosNovo_page_view(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:index'))

    context = {'form': form}

    return render(request, 'website/contactosNovo.html', context)


def jogadorNovo_page_view(request):
    form = JogadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:index'))

    context = {'form': form}

    return render(request, 'website/jogadorNovo.html', context)


def contactosEdita_page_view(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    form = ContactoForm(request.POST or None, instance=contacto)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contactos'))
    context = {'form': form, 'contacto_id': contacto_id}

    return render(request, 'website/contactosEdita.html', context)


def contactosApaga_page_view(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id).delete()

    return HttpResponseRedirect(reverse('website:index'))


def comentarios_page_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:index'))

    context = {'form': form}

    return render(request, 'website/comentarios.html', context)


def resultadosQuizz_page_view(form):
    pontosTotal = 0
    pontosP1 =''
    pontosP2 =''
    pontosP3 =''
    pontosP4 =''
    pontosP5 =''
    pontosP6 =''
    pontosP7 =''
    pontosP8 =''
    pontosP9 =''
    pontosP10 =''

    if form.cleaned_data['p1'] == '2':
        pontosTotal += 1
        pontosP1 = 'Na 1º pergunta obteve: 1 pontos'
    else:
        pontosP1 = 'Na 1º pergunta obteve: 0 pontos'

    if form.cleaned_data['p2'] == '2':
        pontosTotal += 1
        pontosP2 = 'Na 2º pergunta obteve: 1 pontos'
    else:
        pontosP2 = 'Na 2º pergunta obteve: 0 pontos'

    if form.cleaned_data['p3'] == 'Barcelona' or form.cleaned_data['p3'] == 'barcelona' or form.cleaned_data['p3'] == 'Futebol Club Barcelona' or form.cleaned_data['p3'] == 'futebol club barcelona':
        pontosTotal += 1
        pontosP3 = 'Na 3º pergunta obteve: 1 pontos'
    else:
        pontosP3 = 'Na 3º pergunta obteve: 0 pontos'

    if form.cleaned_data['p4'] == '3':
        pontosTotal += 1
        pontosP4 = 'Na 4º pergunta obteve: 1 pontos'
    else:
        pontosP4 = 'Na 4º pergunta obteve: 0 pontos'

    if form.cleaned_data['p5'] == '3':
        pontosTotal += 1
        pontosP5 = 'Na 5º pergunta obteve: 1 pontos'
    else:
        pontosP5 = 'Na 5º pergunta obteve: 0 pontos'

    if form.cleaned_data['p6'] == '3':
        pontosTotal += 1
        pontosP6 = 'Na 6º pergunta obteve: 1 pontos'
    else:
        pontosP6 = 'Na 6º pergunta obteve: 0 pontos'

    if form.cleaned_data['p7'] == 13:
        pontosTotal += 1
        pontosP7 = 'Na 7º pergunta obteve: 1 pontos'
    else:
        pontosP7 = 'Na 7º pergunta obteve: 0 pontos'

    if form.cleaned_data['p8'] == 'Portugal' or form.cleaned_data['p8'] == 'portugal':
        pontosTotal += 1
        pontosP8 = 'Na 8º pergunta obteve: 1 pontos'
    else:
        pontosP8 = 'Na 8º pergunta obteve: 0 pontos'

    if form.cleaned_data['p9'] == '1':
        pontosTotal += 1
        pontosP9 = 'Na 9º pergunta obteve: 1 pontos'
    else:
        pontosP9 = 'Na 9º pergunta obteve: 0 pontos'

    if form.cleaned_data['p10'] == 5:
        pontosTotal += 1
        pontosP10 = 'Na 10º pergunta obteve: 1 pontos'
    else:
        pontosP10 = 'Na 10º pergunta obteve: 0 pontos'

    strResultado = "No total obteve: {TOTAL}".format(TOTAL=pontosTotal)

    pontos = [pontosP1, pontosP2, pontosP3, pontosP4, pontosP5, pontosP6, pontosP7, pontosP8, pontosP9, pontosP10, strResultado]
    return pontos


def quizz_page_view(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        form.save()
        pontos = resultadosQuizz_page_view(form)
        return render(request, 'website/resultadosQuizz.html', {'pontos': pontos})

    context = {'form': form}

    return render(request, 'website/quizz.html', context)


def sobre_page_view(request):
    return render(request, 'website/sobre.html')


def bernabeu_page_view(request):
    return render(request, 'website/paginas/bernabeu.html')


def alvalade_page_view(request):
    return render(request, 'website/paginas/alvalade.html')


def trafford_page_view(request):
    return render(request, 'website/paginas/trafford.html')


def figo_page_view(request):
    return render(request, 'website/paginas/figo.html')


def zidane_page_view(request):
    return render(request, 'website/paginas/zidane.html')


def ronaldo_page_view(request):
    return render(request, 'website/paginas/ronaldo.html')


def ronaldinho_page_view(request):
    return render(request, 'website/paginas/ronaldinho.html')


def sporting_page_view(request):
    return render(request, 'website/paginas/sporting.html')


def juventus_page_view(request):
    return render(request, 'website/paginas/juventus.html')


def united_page_view(request):
    return render(request, 'website/paginas/united.html')


def madrid_page_view(request):
    return render(request, 'website/paginas/madrid.html')


def multimedia_page_view(request):
    return render(request, 'website/multimedia.html')


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
        "autor": "Antonio",
        "bio": "Lionel Andrés Messi Cuccittini (Rosário, 24 de junho de 1987), mais conhecido como Leo Messi, ou apenas como Messi, é um futebolista argentino que atua como atacante ou meia ofensivo."
    },
    {
        "nome": "Joao",
        "apelido": "Palhinha",
        "clube": "Sporting",
        "autor": "Antonio",
        "bio": "João Maria Lobo Alves Palhares Costa Palhinha Gonçalves (Lisboa, 9 de julho de 1995), mais conhecido como João Palhinha, é um futebolista português que atua como volante. Atualmente, joga pelo Sporting e pela Seleção Portuguesa."
    },
    {
        "nome": "Pedro",
        "apelido": "Gonçalves",
        "clube": "Sporting",
        "autor": "Antonio",
        "bio": "Pedro António Pereira Gonçalves, mais conhecido como Pedro Gonçalves ou pelo apelido Pote (Chaves, 28 de junho de 1998) é um futebolista português que atua como meio-campo ou ponta-direita. Atualmente, joga pelo Sporting."
    },
    {
        "nome": "Sergio",
        "apelido": "Oliveira",
        "clube": "Porto",
        "autor": "Antonio",
        "bio": "Sérgio Miguel Relvas de Oliveira é um futebolista português internacional que joga a médio e actualmente no Futebol Clube do Porto. Regressou em 2015/2016 para o FC Porto, clube no qual jogou 10 anos."
    },
    {
        "nome": "Mehdi",
        "apelido": "Taremi",
        "clube": "Porto",
        "autor": "Antonio",
        "bio": "Mehdi Taremi (Bushehr, 18 de julho de 1992), é um futebolista iraniano que atua como atacante. Atualmente, joga pelo Porto."
    },
    {
        "nome": "Julian",
        "apelido": "Weigl",
        "clube": "Benfica",
        "autor": "Antonio",
        "bio": "Julian Weigl (Bad Aibling, 8 de setembro de 1995) é um futebolista alemão que atua como volante. Defende atualmente o Benfica."
    },
    {
        "nome": "Lucas",
        "apelido": "Verissimo",
        "clube": "Benfica",
        "autor": "Antonio",
        "bio": "Lucas Veríssimo da Silva, mais conhecido apenas como Lucas Veríssimo, é um futebolista brasileiro que atua como zagueiro. Atualmente, joga pelo Benfica."
    },
    {
        "nome": "Joao",
        "apelido": "Novais",
        "clube": "Braga",
        "autor": "Antonio",
        "bio": "Nome completo:	João Pedro Barradas Novais, Data de nascimento:	10/07/1993, Local de nascimento: Vila Nova de Gaia  Posição: Médio - Médio Ofensivo"
    },
    {
        "nome": "Lucas",
        "apelido": "Piazon",
        "clube": "Braga",
        "autor": "Antonio",
        "bio": "Lucas Domingues Piazon é um futebolista brasileiro que atua como atacante. Atualmente joga pelo Braga. "
    }
]


def section(request, num):
    if num == 1:
        return JsonResponse({"jogadores": bdJogadores})
    if num == 2:
        return HttpResponse(bdJogadores)
    else:
        raise Http404("No such section")




# Create your views here.
