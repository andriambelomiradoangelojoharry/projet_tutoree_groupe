from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.liste_livre , name="liste_livre"),#le liste any @ views
    path('ajouter/', views.ajouter_livre , name="ajouter_livre"),
    path('recherche/', views.recherche, name='recherche'),
    path("modifier/<int:id>/", views.modifier_livres, name="modifier_livres"),
    path("supprimer/<int:id>/", views.supprimer_livres, name="supprimer_livres"),
]