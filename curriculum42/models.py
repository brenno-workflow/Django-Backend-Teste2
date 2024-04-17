from django.db import models

# Create your models here.

# Aqui vamos criar as tabelas do banco de dados
from django.urls import reverse

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):

        # Retorna para a tela de criação
        #return reverse("user-new")
        
        # Vai direto para a tela de listagem
        return reverse("user-list")
    
