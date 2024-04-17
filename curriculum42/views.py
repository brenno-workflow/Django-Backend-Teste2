from django.shortcuts import render

# Create your views here.

# Criar ações para atualizar o bancod e dados
from django.views import generic
from curriculum42.models import User

class UserNew(generic.CreateView):
    model = User
    fields = '__all__'

class UserList(generic.ListView):
    model = User
    queryset = User.objects.all()