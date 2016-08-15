from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from apps.grupomuscular.models import Grupomuscular

# Create your views here.

def index(request):
	return render(request, 'grupomuscular/index.html')

class GrupoListView (ListView):
	model = Grupomuscular

class GrupoDetailView (DetailView):
	model = Grupomuscular
