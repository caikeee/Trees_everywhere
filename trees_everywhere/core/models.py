import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models import CASCADE

# Custom User model extending AbstractUser to allow additional fields in the future
class User(AbstractUser):
    # Não é necessário ter uma referência OneToOneField ao próprio User
    account = models.ForeignKey("Account", on_delete=CASCADE, blank=True, null=True)
    pass

# Model representing an account in the system
class Account(models.Model):
    # Name of the account
    name = models.CharField(max_length=255)
    # Creation date of the account
    created_at = models.DateTimeField(default=timezone.now)
    # Indicates whether the account is active
    active = models.BooleanField(default=True)

    # Many-to-many relation between users and accounts
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='accounts')

    def __str__(self):
        return self.name  # Retorna o nome da conta

# Model representing a user profile
class Profile(models.Model):
    # One-to-one relationship with the user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Additional information about the user
    about = models.TextField(default="No description")
    # Date the user joined the system
    joined = models.DateTimeField(default=timezone.now)

# Model representing a tree
class Tree(models.Model):
    # Common name of the tree
    name = models.CharField(max_length=255)
    # Scientific name of the tree
    scientific_name = models.CharField(max_length=255)
    
    # String representation of the tree model
    def __str__(self):
        return self.name

# Model representing a tree planted by a user
class PlantedTree(models.Model):
    # Age of the tree in years
    age = models.IntegerField()
    # Timestamp when the tree was planted
    planted_at = models.DateTimeField(auto_now_add=True)
    # Reference to the user who planted the tree
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='planted_trees'
    )
    # Reference to the type of tree planted
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    # Latitude of the location where the tree was planted
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    # Longitude of the location where the tree was planted
    location_long = models.DecimalField(max_digits=9, decimal_places=6)

# Adds a method to the User model for planting a single tree
User.add_to_class(
    'plant_tree', 
    lambda self, tree, location: PlantedTree.objects.create(
        user=self, 
        tree=tree, 
        location_lat=location[0], 
        location_long=location[1]
    )
)

# Adds a method to the User model for planting multiple trees
User.add_to_class(
    'plant_trees', 
    lambda self, plants: [
        self.plant_tree(tree, location) for tree, location in plants
    ]
)
