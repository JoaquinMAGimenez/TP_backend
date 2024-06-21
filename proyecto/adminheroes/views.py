from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from adminheroes.forms import SuperheroeForm, UniversoForm
from adminheroes.models import Superheroe
from adminheroes.serializers import Superheroe
from adminheroes.serializers import HeroesSerializer, UniversoSerializer
# Create your views here.
from models import Superheroe
from models import Universo

def get_all_superheroes():
    superheroes = Superheroe.objects.all().order_by('nombre')
    superheroes_serializer = Superheroe(superheroes, many=True)
    return superheroes_serializer.data

def get_all_universos():
    universos = Universo.objects.all().order_by('name')
    universos_serializer = UniversoSerializer(universos, many=True)
    return universos_serializer.data

def superheroes_rest(request):
    superheroes = Superheroe.objects.all()
    serializer = Superheroe(superheroes, many=True)
    return JsonResponse(serializer.data, safe=False)

def universos_rest(request):
    universos = Universo.objects.all()
    serializer = UniversoSerializer(universos, many=True)
    return JsonResponse(serializer.data, safe=False)

class NewSuperheroeView(CreateView):
    model = Superheroe
    form_class = SuperheroeForm
    template_name = 'form_superheroe.html'
    success_url = reverse_lazy('index_superheroe')

class NewUniversoView(CreateView):
    model = Universo
    form_class = UniversoForm
    template_name = 'form_universo.html'
    success_url = reverse_lazy('index_universo')