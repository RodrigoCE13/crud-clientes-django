from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('clientes')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'el usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'las contraseñas no coinciden'
                })

@login_required
#listar clientes
def clientes(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    clientes = Cliente.objects.filter(estado=True)
    if queryset:
        clientes=Cliente.objects.filter(
            Q(nombre__icontains= queryset)|
            Q(razon_social__icontains=queryset)
        ).distinct()   
    clientes=Cliente.objects.all()#en caso de quere mostrar solo los datos del usuario logeado ""Cliente.objects.filter(user=request.user)""
    return render(request, 'clientes.html',{'clientes':clientes})
@login_required
#crear clientes
def create_clientes(request):
    if request.method == 'GET':
        return render(request, 'create_cliente.html', {
            'form': ClienteForm()
        })
    else:
        try:
            form = ClienteForm(request.POST)
            new_cliente = form.save(commit=False)
            new_cliente.user=request.user
            new_cliente.save()
            return redirect('clientes')
        except ValueError:
            return render(request, 'create_cliente.html', {
                'form': ClienteForm,
                'error': 'Error al crear cliente'
            })
@login_required
#editar clientes
def cliente_detail(request, cliente_id):
    if request.method=='GET':
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form=ClienteForm(instance=cliente)
        return render(request, 'cliente_detail.html',{'cliente':cliente, 'form':form})
    else:
        try:
            cliente=get_object_or_404(Cliente, pk=cliente_id)
            form=ClienteForm(request.POST, instance=cliente)
            form.save()
            return redirect('clientes')
        except ValueError:
            return render(request, 'cliente_detail.html', {
                'cliente':cliente,
                'form':form,
                'error': 'Error al editar cliente'
            })

@login_required
#eliminar clientes
def cliente_delete(request, cliente_id):
    cliente=get_object_or_404(Cliente, pk=cliente_id)
    if(request.method=='POST'):
        cliente.delete()
        return redirect('clientes')

@login_required
#cerrar sesion
def signout(request):
    logout(request)
    return redirect('home')

#iniciar sesion
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario y/o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('clientes')
