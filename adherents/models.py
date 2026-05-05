from django.db import models
from django.contrib.auth.models import User


FONCTIONS = [
    ('Etudiant','Etudiant'),
    ('Formateur', 'Formateur'),
    ('Employé', 'Employé')
]


# Create your models here.
class Adherent(models.Model):
    matricule = models.CharField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    #unique = true  Ceci evite la duplication des adresse email
    email = models.EmailField(unique=True)
    fonctions = models.CharField(choices=FONCTIONS)


    def __str__(self):
        return f"{self.matricule} -- {self.nom}"



class CompteAdherent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personne = models.OneToOneField(Adherent, on_delete=models.CASCADE)

    