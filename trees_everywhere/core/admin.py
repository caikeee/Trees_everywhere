from django.contrib import admin
from .models import User, Profile, Account, Tree, PlantedTree

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Account)
admin.site.register(Tree)
admin.site.register(PlantedTree)
