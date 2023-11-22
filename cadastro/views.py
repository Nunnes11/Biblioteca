from django.shortcuts import render, redirect
from .forms import LivroForm
from django.contrib import messages
from .models import Livro

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Livro cadastrado com sucesso!')
            return redirect('listar')
    else:
        form = LivroForm()
        return render(request, 'cadastrar.html', {'form':form})
    
def listar(request):
    livros = Livro.objects.all()
    return render(request, 'listar.html', {'livros':livros})

def atualizar(request, id):
    livro = Livro.objects.get(id=id)
    form = LivroForm(instance=livro)
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Livro atualizado com sucesso!')
            return redirect('listar')
        else:
            return render(request, 'atualizar.html', {'form':form})
    else:
         return render(request, 'atualizar.html', {'form':form})
    
def detalhar(request, id):
    livro = Livro.objects.get(id=id)
    return render(request, 'detalhar.html', {'livro':livro})

def deletar(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect('listar')

    

