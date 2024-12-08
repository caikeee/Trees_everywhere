from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PlantedTree
from .forms import PlantTreeForm



def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        # Cria o formulário com os dados POST
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Tenta autenticar o usuário
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # Se o usuário for autenticado, faz o login
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect('add_tree')  # Redireciona para a página inicial após login
            else:
                # Caso as credenciais sejam inválidas
                messages.error(request, "Credenciais inválidas.")
        else:
            # Se o formulário não for válido
            messages.error(request, "Erro ao autenticar.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def user_trees_view(request):
    """
    View to display all trees planted by the logged-in user.
    """
    planted_trees = PlantedTree.objects.filter(user=request.user)
    return render(request, 'user_trees.html', {'planted_trees': planted_trees})

from django.shortcuts import get_object_or_404



@login_required
def tree_detail_view(request, pk): 
    planted_tree = get_object_or_404(PlantedTree, pk=pk) 
    return render(request, 'tree_detail.html', {'planted_tree': planted_tree})




@login_required
def add_tree_view(request):
    if request.method == 'POST':
        print("Formulário submetido.")
        form = PlantTreeForm(request.POST)
        if form.is_valid():
            print("Formulário válido.")
            planted_tree = form.save(commit=False)
            planted_tree.user = request.user
            planted_tree.save()
            print("Árvore plantada e salva.")
            return redirect('user_trees')
        else:
            print("Formulário inválido:", form.errors)
    else:
        form = PlantTreeForm()
    return render(request, 'add_tree.html', {'form': form})





@login_required
def account_trees_view(request):
    """
    View to display all trees planted in the accounts the user is part of.
    """
    accounts = request.user.accounts.all()
    planted_trees = PlantedTree.objects.filter(user__accounts__in=accounts).distinct()
    return render(request, 'account_trees.html', {'planted_trees': planted_trees})



@api_view(['GET'])
def user_trees_api(request):
    """
    API endpoint para retornar todas as árvores plantadas pelo usuário logado.
    """
    if not request.user.is_authenticated:
        return Response({'error': 'Autenticação necessária'}, status=401)

    # Recupera as árvores plantadas pelo usuário
    planted_trees = PlantedTree.objects.filter(user=request.user)
    data = [
        {
            'id': tree.id,
            'tree': tree.tree,
            'age': tree.age,
            'planted_at': tree.planted_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for tree in planted_trees
    ]

    return Response(data, status=200)


def create_tree(request, form):
    plant_name = form.cleaned_data['tree']
    plant, created = Plant.objects.get_or_create(name=plant_name)
    PlantedTree.objects.create(user=request.user, plant=plant, **form.cleaned_data)
    return redirect('user_trees')


def plant_create_view(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    return render(request, 'plant_form.html', {'form': form})