from django.urls import path
from adminheroes import views

urlpatterns = [
    path('index_heroe', views.index, name='index_heroe'),
    path('heroes_rest/', views.heroes_rest, name='heroes_rest'),
    path('universos_rest/', views.universos_rest, name='universos_rest'),
    
    path('new_heroe/', views.NewHeroeView.as_view(), name='new_heroe'),
    path('new_universo/', views.NewUniversoView.as_view(), name='new_universo'),
]