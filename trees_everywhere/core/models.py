import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    # Campos adicionais aqui
    pass

# Define o modelo Account, representando uma conta no sistema
class Account(models.Model):
    # Nome da conta
    name = models.CharField(max_length=255)
    # Data de criação da conta
    
    created_at = models.DateTimeField(default=timezone.now)
    # Indicador se a conta está ativa
    active = models.BooleanField(default=True)

# Define o modelo Profile, representando o perfil do usuário
class Profile(models.Model):
    # Relação um-para-um com o usuário
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Informações sobre o usuário
    about = models.TextField(default="Sem descrição")
    # Data em que o usuário se juntou
    joined = models.DateTimeField(default=timezone.now)

# Define o modelo Tree, representando uma árvore
class Tree(models.Model):
    # Nome comum da árvore
    name = models.CharField(max_length=255)
    # Nome científico da árvore
    scientific_name = models.CharField(max_length=255)



class PlantedTree(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='planted_trees')
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_long = models.DecimalField(max_digits=9, decimal_places=6)





# Adiciona métodos ao modelo User para plantar árvores
User.add_to_class('plant_tree', lambda self, tree, location: PlantedTree.objects.create(user=self, tree=tree, location_lat=location[0], location_long=location[1]))
User.add_to_class('plant_trees', lambda self, plants: [self.plant_tree(tree, location) for tree, location in plants])
