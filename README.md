# api_magazzino

Per la creazione dell'API, è stato utilizzato il framework Django, 
che permette di creare applicazioni web in Python.
Sono stati utilizzati anche il framework django-rest-framework 
https://www.django-rest-framework.org/ per utilizzare i serializer 
e djoser https://djoser.readthedocs.io/ 
per creare gli endpoint che generano i token.
Per quanto riguarda la documentazione di quest'ultimi rimando al sito ufficiale 
alla specifica pagina https://djoser.readthedocs.io/en/latest/jwt_endpoints.html.

Per l'autenticazione è stato utilizzato il token JWT, che viene generato dal 
endpoint /auth/jwt/create/
e viene passato come header nelle richieste successive.

I file sui quali si è lavorato sono:
    - settings.py
    - urls.py
    - api/urls.py
    - api/views.py
    - api/models.py
    - api/serializers.py




L'API si copone di 4 endpoint:

r'^api/scatole/'
r'^api/scatole/<int:pk>/'
r'^api/unita/'
r'^api/unita/<int:pk>/'


Descrizione

r'^api/scatole/'

    Questo endpoint recupera o crea un elenco di oggetti "Scatola" o crea in base ai permessi dell'utente e
    dati in ingresso.

    Utenti semplici possono listare solo le scatole di cui sono proprietari.
    Superuser puo listare tutte le scatole.

    Per la creazione di un oggetto "Scatola" oltre ad essere autenticati 
    è necessario passare i seguenti dati ("descrizione" puo essere omesso)in ingresso in formato 
    JSON e modalità POST:

     {
        "nome": "r'^[a-zA-Z]+$'",  
        "unita": 1r'^\d+$'
    }
       



r'^api/scatole/<int:pk>/'


    Questo endpoint recupera, aggiorna o elimina un oggetto "Scatola" in base ai permessi 
    dell'utente e dati in ingresso e metodi utilizzati.(pk è la chiave primaria dell'oggetto)



r'^api/unita/'


    Questo endpoint recupera o crea un elenco di oggetti "Unita" o ne crea in base 
    ai permessi dell'utente e dei dati in ingresso.

    Utenti semplici possono listare solo le unita di cui sono proprietari.
    Superuser puo listare tutte le unita e crearle.

    Per la creazione di un oggetto "Unita" oltre ad essere autenticati come superuser 
    è necessario passare i seguenti dati in ingresso in formato JSON e modalità POST:

    { 
        "nome": "r'^[a-zA-Z]+$'",
        "organizzazione": r'^\d+$',
        "max_scatole": r'^\d+$'
    }

r'^api/unita/<int:pk>/'

    Questo endpoint recupera,  o elimina un oggetto "Unita"  in base ai permessi dell'utente e
    dati in ingresso.(pk è la chiave primaria dell'oggetto)
    Per eliminare un oggetto "Unita" oltre ad essere autenticati come superuser





Ulteriore documentazione è presente nel file api/views.py

In particolare c'è la documentazione del funzionamento delle funzioni. 


