from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('senha/', PasswordChange.as_view(template_name='alterar_senha.html'), name='mudar_senha'),
    path('criar/usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('editar/usuario/', UsuarioUpdate.as_view(), name='editar_usuario'),
    path('listar/usuarios/', UsuarioList.as_view(), name='listar_usuarios'),
    path('deletar/usuario/<int:pk>', UsuarioDelete.as_view(), name='deletar_usuario'),
]
