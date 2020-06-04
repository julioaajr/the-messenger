from django.shortcuts import render, redirect
from django.views.decorators.csrf  import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import AuthUser, Amigos, Amizade
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
def del_friend(request):
    data = {}
    data['error'] = []
    if request.method == 'GET':
        id_amizade = int(request.GET.get('id'))
        try:
            amigos = Amigos.objects.get(id=id_amizade)
            amigos.delete()
        except:
            data['error'].append("Erro ao deletar AMIGO! ")
            return redirect(request, '/')
    return redirect('/')





@login_required(login_url='/login/')
def add_friend(request):
    data = {}
    data['error'] = []
    if request.method == 'GET':
        id_amigo = int(request.GET.get('id'))
        id_user = request.user.id
        try:
            myUser = AuthUser.objects.get(id=id_user)
            amigo = AuthUser.objects.get(id=id_amigo)
            amizade = Amizade(myUser=myUser, amigo=amigo)
            amigos = Amigos(myid = id_user, amigo = amigo)
            amizade.save()
            amigos.save()
        except:
            data['error'].append("Erro ao deletar produto! ")
            return redirect('/')
    return redirect('/')


@login_required(login_url='/login/')
def index(request):
    gbusca = request.POST.get('buscaruser')
    data = {}
    data['list'] = []
    data['error'] = []
    data['amigos'] =[]
    data['volta_amigos'] = []
    try:
        usuario = AuthUser.objects.get(id = request.user.id)
        data['amigos'] = Amizade.objects.filter(myUser = usuario)
        data['volta_amigos'] = Amizade.objects.filter(amigo = usuario)
        if(gbusca != ''):
            data['list'] = AuthUser.objects.filter(username__contains = gbusca).exclude(id = request.user.id, amizade__in = data['amigos'].amigo)
            print(data['amigos'])


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
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if (password == repassword):
            user = User.objects.create_user(username=username, email= email, password=password, is_superuser=1, is_staff=1)
            user.save()
            return redirect('/login/')                    
            print('cadastro realiado')
        else:
            messages.error(request, "usuário e senha invalido favor tentar novamente.")
            return redirect('/login/', data)   
