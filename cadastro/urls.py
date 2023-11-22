
from django.urls import path, include
from .views import cadastro, listar, atualizar, detalhar, deletar

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('', listar, name='listar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
    path('detalhar<int:id>', detalhar, name= 'detalhar'),
    path('deletar/<int:id>', deletar, name='deletar'),
]