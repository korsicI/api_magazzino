from django.db import models
from django.contrib.auth.models import User


# Questa è una classe modello Django per collegare utente a un'organizzazione.

class Utente_Organizzazione(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organizzazione = models.ForeignKey('Organizzazione', on_delete=models.CASCADE, related_name='users')
    def __str__(self):
        return self.user.username + ' ' + self.organizzazione.nome
    
    class Meta:
        verbose_name_plural = "Utenti_Organizzazioni"



class Organizzazione(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome
        

    class Meta:
        verbose_name_plural = "Organizzazioni"

class Unita(models.Model):
    nome= models.CharField(max_length=255)
    organizzazione = models.ForeignKey(Organizzazione, on_delete=models.CASCADE, related_name='tutte_unita')
    max_scatole = models.PositiveIntegerField()
    def __str__(self):
        return self.organizzazione.nome + ' ' + str(self.id)
    
    class Meta:
        verbose_name_plural = "Unita"
    


class Scatola(models.Model):
    unita = models.ForeignKey(Unita, on_delete=models.CASCADE, related_name='scatole')
    nome = models.CharField(max_length=255)
    descrizione = models.TextField(blank=True, default='')
    def __str__(self):
        return self.unita.organizzazione.nome + ' ' + str(self.unita.id) + ' ' + self.nome
    
    class Meta:
        verbose_name_plural = "Scatole"
