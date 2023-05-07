from django.contrib import admin

# Register your models here.

from .models import Organizzazione, Utente_Organizzazione, Unita, Scatola

admin.site.register(Organizzazione)
admin.site.register(Utente_Organizzazione)
admin.site.register(Unita)
admin.site.register(Scatola)
