from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account, PlantedTree, Profile
from .forms import AccountForm, PlantTreeForm
from django.shortcuts import render, redirect, get_object_or_404

# Function to render the home page
def home_view(request):
    return render(request, 'home.html')

# Function to handle user login
def login_view(request):
    if request.method == 'POST':
        # Create the form with POST data
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log in the user if authentication is successful
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('user_trees')  # Redirect to user's trees page
            else:
                # Show error message if credentials are invalid
                messages.error(request, "Invalid credentials.")
        else:
            # Show error message if the form is invalid
            messages.error(request, "Authentication error.")
    else:
        # Create an empty form if the method is not POST
        form = AuthenticationForm()

    # Render the login page with the form
    return render(request, 'login.html', {'form': form})

# Protected function to display trees planted by the logged-in user
@login_required
def user_trees_view(request):
    # Retrieve the logged-in user's profile
    profile = Profile.objects.get(user=request.user)
    # Retrieve the trees planted by the logged-in user
    planted_trees = PlantedTree.objects.filter(user=request.user)
    # Render the template with the user's profile and planted trees
    return render(request, 'user_trees.html', {
        'planted_trees': planted_trees,
        'profile': profile
    })

# Protected function to display details of a specific tree
@login_required
def tree_detail_view(request, pk):
    # Get the tree by its primary key or return a 404 if not found
    planted_tree = get_object_or_404(PlantedTree, pk=pk)
    # Render the tree detail page
    return render(request, 'tree_detail.html', {'planted_tree': planted_tree})

# Protected function to add a new tree
@login_required
def add_tree_view(request):
    if request.method == 'POST':
        # Create the form with POST data
        form = PlantTreeForm(request.POST)
        if form.is_valid():
            # Create a new planted tree object without saving to the database
            planted_tree = form.save(commit=False)
            # Associate the tree with the logged-in user
            planted_tree.user = request.user
            # Save the tree to the database
            planted_tree.save()
            return redirect('user_trees')  # Redirect to the user's tree list
    else:
        # Create an empty form if the method is not POST
        form = PlantTreeForm()
    # Render the page with the form
    return render(request, 'add_tree.html', {'form': form})

# Protected function to display trees planted in accounts the user is part of
@login_required
def account_tree_view(request, name):
    # Retrieve the account by its name
    account = get_object_or_404(Account, name=name)  # Busca a conta pelo campo 'name'
    
    # Retrieve trees planted by users in this account
    planted_trees = PlantedTree.objects.filter(user__accounts=account).distinct()
    
    # Render the page with the account and planted trees
    return render(request, 'account_tree.html', {'account': account, 'planted_trees': planted_trees})


# API to return trees planted by the logged-in user
@api_view(['GET'])
def user_trees_api(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=401)

    # Retrieve trees planted by the user
    planted_trees = PlantedTree.objects.filter(user=request.user)
    # Serialize tree data into JSON format
    data = [
        {
            'id': tree.id,
            'tree': tree.tree,
            'age': tree.age,
            'planted_at': tree.planted_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for tree in planted_trees
    ]

    # Return data in JSON format with status 200
    return Response(data, status=200)

# Function to create a tree associated with a user and specific plant
def create_tree(request, form):
    # Retrieve the plant name from the form
    plant_name = form.cleaned_data['tree']
    # Get or create a plant with the given name
    plant, created = Plant.objects.get_or_create(name=plant_name)
    # Create a PlantedTree instance associated with the user and plant
    PlantedTree.objects.create(user=request.user, plant=plant, **form.cleaned_data)
    # Redirect to the user's tree list
    return redirect('user_trees')

# Function to create a new plant (not directly associated with a user)
def plant_create_view(request):
    if request.method == 'POST':
        # Create the form with POST data
        form = PlantForm(request.POST)
        if form.is_valid():
            # Save the new plant to the database
            form.save()
            return redirect('plant_list')  # Redirect to the plant list
    else:
        # Create an empty form if the method is not POST
        form = PlantForm()
    # Render the page with the plant creation form
    return render(request, 'plant_form.html', {'form': form})

# View para listar todas as accounts
def account_list_view(request):
    # Recupera todas as instâncias do modelo Account
    accounts = Account.objects.all()
    
    # Passa as accounts para o template
    return render(request, 'account_list.html', {'accounts': accounts})

# View para criar uma nova conta
@login_required  # Garante que apenas usuários autenticados possam acessar essa página
def create_account(request):
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados recebidos
        form = AccountForm(request.POST)
        if form.is_valid():
            # Salva o formulário e cria a nova conta
            form.save()
            # Redireciona para a lista de contas ou outra página de sucesso
            return redirect('account_list')
    else:
        # Se o método não for POST, apenas exibe o formulário vazio
        form = AccountForm()

    # Renderiza o template com o formulário
    return render(request, 'account/account_list.html', {'form': form})