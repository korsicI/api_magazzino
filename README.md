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
endpoint /auth/jwt/create/ e viene passato come header nelle richieste successive.

Nei setting e stato modificato timedelta per facilitare il controllo.

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
   'ACCESS_TOKEN_LIFETIME': timedelta(days=1)
}

Ulteriore documentazione è presente nel file api/views.py
In particolare c'è la documentazione del funzionamento delle funzioni.

Per mantenere il file leggibile e di facile comprensione, ho preferito limitare l'uso delle funzioni 
solo ai casi strettamente necessari, in modo da rendere il codice più accessibile e comprensibile per la valutazione.
Normalmente utilizzo decoratori, generatori, moduli e altre tecniche avanzate di Python.
Posso anche confermare di avere familiarità con le librerie NumPy e Matplotlib, 
che sono strumenti potenti per l'elaborazione numerica e la visualizzazione dei dati in Python.


I file sui quali si è lavorato sono:
    - settings.py
    - urls.py
    - api/urls.py
    - api/views.py
    - api/models.py
    - api/serializers.py




L'API si copone di 4 endpoint:

1. r'^api/scatole/'
2. r'^api/scatole/<int:pk>/'
3. r'^api/unita/'
4. r'^api/unita/<int:pk>/'


Descrizione

1. r'^api/scatole/'

    Questo endpoint recupera o crea un elenco di oggetti "Scatola" o crea in base ai permessi dell'utente e
    dati in ingresso.

    Utenti semplici possono visualizzare solo le scatole di cui sono proprietari.
    Superuser puo listare tutte le scatole.

    Per la creazione di un oggetto "Scatola" oltre ad essere autenticati 
    è necessario passare i seguenti dati ("descrizione" puo essere omesso)in ingresso in formato 
    JSON e modalità POST:

     {
        "nome": "r'^[a-zA-Z]+$'",  
        "unita": 1r'^\d+$'
    }
       



2. r'^api/scatole/<int:pk>/'


    Questo endpoint recupera, aggiorna o elimina un oggetto "Scatola" in base ai permessi 
    dell'utente e dati in ingresso e metodi utilizzati.(pk è la chiave primaria dell'oggetto)



3. r'^api/unita/'


    Questo endpoint recupera o crea un elenco di oggetti "Unita" o ne crea in base 
    ai permessi dell'utente e dei dati in ingresso.

    Utenti semplici possono visualizzare solo le unita di cui sono proprietari.
    Mentre gli amministratori possono visualizzare e creare tutte le unità. 

    Per la creazione di un oggetto "Unita" oltre ad essere autenticati come superuser 
    è necessario passare i seguenti dati in ingresso in formato JSON e modalità POST:

    { 
        "nome": "r'^[a-zA-Z]+$'",
        "organizzazione": r'^\d+$',
        "max_scatole": r'^\d+$'
    }

4. r'^api/unita/<int:pk>/'

    Questo endpoint recupera o elimina un oggetto "Unita" in base ai permessi dell'utente 
    e ai dati in ingresso. "pk" rappresenta la chiave primaria dell'oggetto. 
    Per eliminare un oggetto "Unita", è necessario essere autenticati come amministratori.








