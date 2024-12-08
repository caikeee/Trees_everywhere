from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal

class User(AbstractUser):
    """Usuário do sistema"""
    def plant_tree(self, plant, location):
        """Planta uma árvore"""
        latitude, longitude = location
        planted_tree = PlantedTree.objects.create(
            user=self, 
            plant=plant,
            latitude=Decimal(latitude), 
            longitude=Decimal(longitude)
        )
        return planted_tree

class Profile(models.Model):
    """Perfil do usuário"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class Account(models.Model):
    """Conta"""
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    members = models.ManyToManyField(User, related_name='accounts')

    def __str__(self):
        return self.name

class Plant(models.Model):
    """Planta"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PlantedTree(models.Model):
    """Árvore plantada"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planted_trees')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='planted_trees')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    date_planted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plant.name} plantada por {self.user.username}"