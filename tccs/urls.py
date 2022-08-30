from django.urls import path

from .views import *

urlpatterns = [
    path('', TccList.as_view(), name='index'),

    path('criar/autor/', AutorCreate.as_view(), name='criar_autor'),
    path('criar/curso/', CursoCreate.as_view(), name='criar_curso'),
    path('criar/orientador/', OrientadorCreate.as_view(), name='criar_orientador'),
    path('criar/tcc/', TccCreate.as_view(), name='criar_tcc'),

    path('editar/autor/<int:pk>/', AutorUpdate.as_view(), name='editar_autor'),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name='editar_curso'),
    path('editar/orientador/<int:pk>/', OrientadorUpdate.as_view(), name='editar_orientador'),
    path('editar/tcc/<int:pk>/', TccUpdate.as_view(), name='editar_tcc'),
    
    path('listar/autores/', AutorList.as_view(), name='listar_autores'),
    path('listar/cursos/', CursoList.as_view(), name='listar_cursos'),
    path('listar/orientadores/', OrientadorList.as_view(), name='listar_orientadores'),
    
    path('deletar/autor/<int:pk>/', AutorDelete.as_view(), name='deletar_autor'),
    path('deletar/curso/<int:pk>/', CursoDelete.as_view(), name='deletar_curso'),
    path('deletar/orientador/<int:pk>/', OrientadorDelete.as_view(), name='deletar_orientador'),
    path('deletar/tcc/<int:pk>/', TccDelete.as_view(), name='deletar_tcc'),

    path('detalhar/tcc/<int:pk>', TccDetail.as_view(), name='detalhar_tcc'),
]
