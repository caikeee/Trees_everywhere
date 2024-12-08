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
                return redirect('user_trees')  # Redireciona para a página inicial após login
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
def tree_detail_view(request, tree_id):
    """
    View to display details of a specific planted tree.
    """
    tree = get_object_or_404(PlantedTree, id=tree_id, user=request.user)
    return render(request, 'tree_detail.html', {'tree': tree})




@login_required
def add_tree_view(request):
    if request.method == 'POST':
        form = PlantTreeForm(request.POST)
        if form.is_valid():
            planted_tree = form.save(commit=False)
            planted_tree.user = request.user
            planted_tree.save()
            return redirect('user_trees')
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
    API endpoint to return all trees planted by the logged-in user.
    """
    if not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=401)

    # Recupera as árvores plantadas pelo usuário
    planted_trees = PlantedTree.objects.filter(user=request.user)
    data = [
        {
            'id': tree.id,
            'plant_name': tree.plant.name,
            'latitude': float(tree.latitude),
            'longitude': float(tree.longitude),
            'date_planted': tree.date_planted.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for tree in planted_trees
    ]

    return Response(data, status=200)