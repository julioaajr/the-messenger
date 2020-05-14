from django.shortcuts import render, redirect
from django.views.decorators.csrf  import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import AuthUser, Amizade, Amigos
from datetime import date
# Create your views here.


def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "usuário e senha invalido favor tentar novamente.")
    return redirect('/login/')

@login_required(login_url='/login/')
def add_friend(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'GET':
        id_amigo = int(request.GET.get('id'))
        id_user = request.user.id
        try:
            amigo = AuthUser.objects.get(id=id_amigo)
            amigos = Amigos(myid = id_user, amigo = amigo )
            amigos.save()
        except:
            data['error'].append("Erro ao deletar produto! ")
            return redirect(request, '/')
    return redirect('/')


@login_required(login_url='/login/')
def index(request):
    data = {}
    data['list'] = []
    data['error'] = []
    data['amigos'] =[]
    print(request.user.username)
    try:
        #data['amigos'] = Amizade.objects.all()
        data['list'] = User.objects.all()
        print(data)

    except:
         data['error'].append("Erro ao carregar Usuario! ")
    return render(request, 'index.html', data)

def logout_user(request):
    logout(request)
    return redirect('/login/')


def registrar(request):
    return render(request, 'registrar.html')

@csrf_exempt
def submit_registrar(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        #user = AuthUser(password=password, username=username, is_superuser=False, first_name='', email='', is_staff=False, date_joined='',last_name='')
        user = User.objects.create_user(username=username, password=password, is_superuser=1, is_staff=1)
        user.save()

    return redirect('/login/')