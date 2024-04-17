from django.contrib import admin

# Register your models here.

# Informar as aplicações para aparecer no admin
from curriculum42.models import User

admin.site.register(User)
