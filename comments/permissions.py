from rest_framework import permissions
from .models import Comment
from rest_framework.views import View
from rest_framework.request import Request


# pode editar e deletar se for o dono, caso dono do post pode deletar e qlqr um pode ler
