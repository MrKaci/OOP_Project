# Register your models here.
from django.contrib import admin
from . import models

admin.site.register(models.Ville)
admin.site.register(models.Produit)
admin.site.register(models.Ressource)
admin.site.register(models.QuantiteRessource)
admin.site.register(models.Usine)
admin.site.register(models.Machine)
admin.site.register(models.SiegeSocial)
admin.site.register(models.Etape)
admin.site.register(models.Stock)
