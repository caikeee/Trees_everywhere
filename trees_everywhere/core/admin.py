from django.contrib import admin
from .models import User, Profile, Account, Plant, PlantedTree

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Account)
admin.site.register(Plant)
admin.site.register(PlantedTree)
