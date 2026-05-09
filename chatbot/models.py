from django.db import models
from adherents.models import Adherent


class HistoriqueChat(models.Model):
    adherent  = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    role      = models.CharField(choices=[
                    ('user', 'User'),
                    ('bot',  'Bot'),
                ], max_length=10)
    message   = models.TextField()
    date      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']