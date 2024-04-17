from django.shortcuts import render

# Create your views here.

# Criar ações para atualizar o bancod e dados
from django.views import generic
from curriculum42.models import User
from django.urls import reverse_lazy

class UserNew(generic.CreateView):
    model = User
    fields = '__all__'

class UserList(generic.ListView):
    model = User
    queryset = User.objects.all()

class UserUpdate(generic.UpdateView):
    model = User
    fields = ['username', 'email']
    template_name_sufix  = 'update_form'

class UserDetail(generic.DetailView):
    model = User

class UserDelete(generic.DeleteView):
    model = User
    success_url = reverse_lazy('user-list')