from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('autor/', views.autor_lista, name='autor_lista'),
    path('autor/adicionar/', views.autor_add, name='autor_add'),
    path('autor/editar/<int:autor_pk>', views.autor_edit, name='autor_edit'),
    path('autor/deletar/<int:autor_pk>', views.autor_del, name='autor_del'),

    path('livro/', views.livro_lista, name='livro_lista'),
    path('livro/adicionar/', views.livro_add, name='livro_add'),
    path('livro/editar/<int:livro_pk>', views.livro_edit, name='livro_edit'),
    path('livro/deletar/<int:livro_pk>', views.livro_del, name='livro_del'),

    path('editora/', views.editora_lista, name='editora_lista'),
    path('editora/adicionar/', views.editora_add, name='editora_add'),
    path('editora/editar/<int:editora_pk>', views.editora_edit, name='editora_edit'),
    path('editora/deletar/<int:editora_pk>', views.editora_del, name='editora_del'),

    path('formato/', views.formato_lista, name='formato_lista'),
    path('formato/adicionar/', views.formato_add, name='formato_add'),
    path('formato/editar/<int:formato_pk>', views.formato_edit, name='formato_edit'),
    path('formato/deletar/<int:formato_pk>', views.formato_del, name='formato_del'),

    path('dashboard/', views.dashboard, name='dashboard'),    
]