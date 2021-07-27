from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
from website.models import Contacto


def index_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
        context = {'contactos': Contacto.objects.all()}
        return render(request, "website/contactos.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
                    request,
                    username=username,
                    password=password
        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('website:contactos'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Credenciais inválidas.'
            })

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'website/index.html', {
        'message': 'Logged out'})
