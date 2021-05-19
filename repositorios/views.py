from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from repositorios.createUser import UserForm
from django.views.generic.list import ListView
from django.http import HttpResponse

from repositorios.models import Usuario, Repositorio


# Create your views here.

def list_repositorio(request):
	repositorio = Repositorio.objects.all()
	return render(request, template_name='index_repositorios.html', context={'repositorio':repositorio})



class UserCreate(CreateView):
	model = Usuario
	form_class = UserForm
	template_name = 'add_user.html'

	def get_success_url(self):
		return reverse('repositorios:index_repositorios')

def buscar_repositorios(request):
	return render(request, "buscar_repositorio.html")

def buscar(request):
	mensaje = "Repositorio buscado: %r" % request.GET['git']
	return HttpResponse(mensaje)