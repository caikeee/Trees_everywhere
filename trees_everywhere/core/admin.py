from django.contrib import admin
from .models import User, Profile, Account, Tree, PlantedTree

# Registers the User model to be manageable via the Django admin interface
admin.site.register(User)

# Registers the Profile model to enable admin management of user profiles
admin.site.register(Profile)

# Registers the Account model to allow management of accounts in the admin panel
admin.site.register(Account)

# Registers the Tree model to manage tree records in the admin interface
admin.site.register(Tree)

# Registers the PlantedTree model to track planted trees through the admin panel
admin.site.register(PlantedTree)
