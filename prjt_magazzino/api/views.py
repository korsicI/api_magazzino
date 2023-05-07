from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Scatola,Unita, Utente_Organizzazione
from .serializers import ScatolaSerializer, UnitaSerializer




@api_view(['GET', 'POST'])
def scatola_list(request):
    """
    Questa funzione recupera o crea un elenco di oggetti "Scatola" o crea in base ai permessi dell'utente e
    dati in ingresso.
    
    :param request: L'oggetto di richiesta HTTP che contiene informazioni sulla richiesta effettuata, ad esempio
    intestazione e dati.

    :return: Un oggetto Response con dati serializzati e codice di stato HTTP.
    """
    user = request.user
    user_utente = Utente_Organizzazione.objects.get(user=user)
    if request.method == 'GET': 
        if user.is_superuser:
            scatole = Scatola.objects.all()
            serializer = ScatolaSerializer(scatole, many=True)
            return Response(serializer.data)
    
        else:
            
            scatole = Scatola.objects.filter(unita__organizzazione=user_utente.organizzazione)
            serializer = ScatolaSerializer(scatole, many=True)
            return Response(serializer.data)
        
    elif request.method == 'POST':
        if user.is_superuser:
            serializer = ScatolaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ScatolaSerializer(data=request.data)
            serializer = ScatolaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data
            #scriver match per 0 o max_boxes
            if user_utente.organizzazione == serializer.validated_data.get('unita').organizzazione and serializer.validated_data.get('unita').scatole.count() < serializer.validated_data.get('unita').max_scatole:
                serializer.save()
                return Response('tutto ok')
            else:
                return Response('Utente non abilitato ',status=status.HTTP_403_FORBIDDEN)



@api_view(['GET', 'DELETE'])
def scatola_detaglio(request, pk):
    """
    Questa funzione recupera o elimina uno specifico oggetto "Scatola" in base ai permessi dell'utente e
    ingresso.
    
    :param request: L'oggetto di richiesta HTTP che contiene informazioni sulla richiesta effettuata, ad esempio
    come il metodo HTTP (GET, POST, DELETE, ecc.), le intestazioni e tutti i dati inclusi nella richiesta
    
    :param pk: pk è un parametro che sta per "chiave primaria". In questo contesto, si riferisce all'unico
    identificatore di una specifica istanza del modello Scatola (che è un modello Django). La chiave primaria è
    utilizzato per recuperare o eliminare un'istanza specifica del modello dal database
    
    :return: questo codice restituisce un oggetto risposta con dati serializzati o un codice di stato HTTP a seconda
    sul metodo di richiesta e sui permessi dell'utente. Se il metodo di richiesta è GET e l'utente è autorizzato
    per accedere all'oggetto Scatola richiesto, vengono restituiti i dati serializzati dell'oggetto Scatola. Se
    il metodo di richiesta è DELETE e l'utente è autorizzato a cancellare l'oggetto Scatola richiesto, il
    l'oggetto viene eliminato dal database e viene restituito un codice di stato HTTP 204 (senza contenuto). Se
    l'oggetto Scatola richiesto non esiste, viene restituito un codice di stato HTTP 404 (non trovato). Se l'utente
    non è autorizzato a recuperare o eliminare l'oggetto Scatola richiesto, viene restituito un codice di stato HTTP 403 (proibito).
   
    """

    user = request.user
    user_utente = Utente_Organizzazione.objects.get(user=user)
    if request.method == 'GET':
        try:
            scatola = Scatola.objects.get(pk=pk)
            if user.is_superuser:
                serializer = ScatolaSerializer(scatola, many=False)
                return Response(serializer.data)
            else:
                if scatola.unita.organizzazione == user_utente.organizzazione:
                    serializer = ScatolaSerializer(scatola, many=False)
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
        except Scatola.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    elif request.method == 'DELETE':
        try:
            scatola = Scatola.objects.get(pk=pk)
            if user.is_superuser:
                scatola.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                if scatola.unita.organizzazione == user_utente.organizzazione:
                    scatola.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
        except Scatola.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET', 'POST'])

def unita_list(request):
    """ 
    Questa è una funzione che restituisce un elenco di unità in base alle autorizzazioni e ai permessi dell'utente.
    E per la creazione di nuove unità se l'utente è un superutente.

    :param request: L'oggetto di richiesta HTTP che contiene informazioni sulla richiesta effettuata, ad esempio
    come il metodo HTTP (GET, POST, DELETE, ecc.), le intestazioni e tutti i dati inclusi nella richiesta

    :return: questo codice restituisce un oggetto risposta con dati serializzati o un codice di stato HTTP a seconda
    sul metodo di richiesta e sui permessi dell'utente. Se il metodo di richiesta è GET e l'utente è autorizzato
    per accedere all'oggetto unità richiesto, vengono restituiti i dati serializzati dell'oggetto unità. Se
    il metodo di richiesta è POST e l'utente è autorizzato a creare un'unità, l'unità viene creata e viene restituito un codice di stato HTTP 201 (creato). Se
    l'utente non è autorizzato a recuperare o creare l'oggetto unità richiesto, viene restituito un codice di stato HTTP 403 (proibito).
    
    """
    user = request.user
    user_utente = Utente_Organizzazione.objects.get(user=user)
    if request.method == 'GET': 
        if user.is_superuser:
            unita = Unita.objects.all()
            serializer = UnitaSerializer(unita, many=True)
            return Response(serializer.data)
    
        else:
            
            unita = Unita.objects.filter(organizzazione=user_utente.organizzazione)
            serializer = UnitaSerializer(unita, many=True)
            return Response(serializer.data)
        
    elif request.method == 'POST':
        if user.is_superuser:
            serializer = UnitaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Utente non abilitato ',status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'DELETE'])
def unita_detaglio(request, pk):
    """
    Questa è una funzione che restituisce o cancella un unità in base alle autorizzazioni e ai permessi dell'utente.

    :param request: L'oggetto di richiesta HTTP che contiene informazioni sulla richiesta effettuata, ad esempio
    come il metodo HTTP (GET, POST, DELETE, ecc.), le intestazioni e tutti i dati inclusi nella richiesta
    
    :param pk: è la chiave primaria dell'unità che si desidera recuperare o eliminare

    :return: questo codice restituisce un oggetto risposta con dati serializzati o un codice di stato HTTP a seconda
    sul metodo di richiesta e sui permessi dell'utente. Se il metodo di richiesta è GET e l'utente è autorizzato
    per accedere all'oggetto unità richiesto, vengono restituiti i dati serializzati dell'oggetto unità. Se
    il metodo di richiesta è DELETE e l'utente è autorizzato a eliminare l'unità, l'unità viene eliminata e viene restituito un codice di stato HTTP 204 (nessun contenuto). Se
    l'utente non è autorizzato a recuperare o eliminare l'oggetto unità richiesto, viene restituito un codice di stato HTTP 403 (proibito).

    """
    user = request.user
    user_utente = Utente_Organizzazione.objects.get(user=user)
    if request.method == 'GET':
        try:
            unita = Unita.objects.get(pk=pk)
            if user.is_superuser:
                serializer = UnitaSerializer(unita, many=False)
                return Response(serializer.data)
            else:
                if unita.organizzazione == user_utente.organizzazione:
                    serializer = UnitaSerializer(unita, many=False)
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
        except Unita.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    elif request.method == 'DELETE':
        try:
            unita = Unita.objects.get(pk=pk)
            if user.is_superuser:
                unita.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                if unita.organizzazione == user_utente.organizzazione:
                    
                    return Response(status=status.HTTP_403_FORBIDDEN)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
        except Unita.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        



