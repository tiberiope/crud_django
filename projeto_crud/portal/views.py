from django.shortcuts import redirect, render
from portal.models import Autor, Livro, Editora
from portal.forms import AutorForm

# Create your views here.
def home(request):

    return render(request, 'portal/home.html')


# funções do autor.
def autor_lista(request):
    autores = Autor.objects.all()

    conteudo = {
        'autores': autores
    }

    return render(request, 'portal/autor/autor_lista.html', conteudo)


def autor_add(request):
    form = AutorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor_lista')

    conteudo = {
        'form': form
    }

    return render(request, 'portal/autor/autor_add.html', conteudo)


def autor_edit(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    form = AutorForm(request.POST or None, instance=autor)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor_lista')

    conteudo = {
        'form': form,
        'autor': autor
    }

    return render(request, 'portal/autor/autor_edit.html', conteudo)


def autor_del(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    autor.delete()

    return redirect('autor_lista')

# Livros ----------------
def livro_lista(request):

    livros = Livro.objects.all()

    conteudo = {
        'livros': livros
    }

    return render(request, 'portal/livro/livro_lista.html', conteudo)


def livro_add(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        subtitulo = request.POST['subtitulo']
        autor = request.POST['autor']
        data_lancamento = request.POST['data_lancamento']
        isbn = request.POST['isbn']
        numero_paginas = request.POST['numero_paginas']

        livro = Livro.objects.create(titulo=titulo, subtitulo=subtitulo, autor=autor, data_lancamento=data_lancamento, isbn=isbn, numero_paginas=numero_paginas)
        livro.save()
        return redirect('livro_lista')

    return render(request, 'portal/livro/livro_add.html')


# Editora
def editora_lista(request):
    editoras = Editora.objects.all()

    conteudo = {
        'editoras': editoras
    }

    return render(request, 'portal/editora/editora_lista.html', conteudo)


def editora_add(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cidade = request.POST['cidade']
        estado = request.POST['estado']

        editora = Editora.objects.create(nome=nome, cidade=cidade, estado=estado)
        editora.save()

        return redirect('editora_lista')
    
    return render(request, 'portal/editora/editora_add.html')


def editora_edit(request, editora_pk):
    editora = Editora.objects.get(pk=editora_pk)

    if request.POST:
        editora.nome = request.POST['nome']
        editora.cidade = request.POST['cidade']
        editora.estado = request.POST['estado']
        editora.save()
        
        return redirect('editora_lista')

    conteudo = {
        'editora': editora
    }

    return render(request, 'portal/editora/editora_edit.html', conteudo)
    

def editora_del(request, editora_pk):
    editora = Editora.objects.get(pk=editora_pk)

    editora.delete()

    return redirect('editora_lista')

def formato(request):

    return render(request, 'portal/formato.html')

def dashboard(request):

    return render(request, 'portal/dashboard.html')