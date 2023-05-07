from rest_framework import serializers
from .models import Scatola, Organizzazione, User, Utente_Organizzazione, Unita
from django.contrib.auth.models import User

class OrganizzazioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizzazione
        fields = ['id', 'nome']

class ScatolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scatola
        fields = ['id', 'nome', 'descrizione', 'unita']

class UnitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unita
        fields = ['id', 'nome', 'organizzazione', 'max_boxes']
 
