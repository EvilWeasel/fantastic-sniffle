from django.contrib import admin
from .models import Katalog, Frage, Teilnehmer, Admin, Fragebogen

# Register your models here.

admin.site.register(Katalog)
admin.site.register(Frage)
admin.site.register(Teilnehmer)
admin.site.register(Admin)
admin.site.register(Fragebogen)
