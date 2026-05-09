from django.urls import path
from . import views

urlpatterns = [
    path("", views.chatbot, name='chatbot'),
    path("historique", views.charger_historique, name="chargerHistorique")
]
