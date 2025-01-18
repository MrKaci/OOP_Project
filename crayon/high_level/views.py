# Create your views here.
from django.views.generic import DetailView
from django.http import JsonResponse
from .models import (
    Machine,
    Usine,
    Ressource,
    Stock,
    Ville,
    QuantiteRessource,
    Etape,
    Produit,
    SiegeSocial,
)


class MachineDetailView(DetailView):
    model = Machine

    def get(self, request, *args, **kwargs):
        machine = self.get_object()
        data = {
            "nom": machine.nom,
            "prix": machine.prix,
            "n_serie": machine.n_serie,
        }
        return JsonResponse(data)


class UsineDetailView(DetailView):
    model = Usine

    def get(self, request, *args, **kwargs):
        usine = self.get_object()
        return JsonResponse(usine.json())


class RessourceDetailView(DetailView):
    model = Ressource

    def get(self, request, *args, **kwargs):
        ressource = self.get_object()
        return JsonResponse(ressource.json())


class StockDetailView(DetailView):
    model = Stock

    def get(self, request, *args, **kwargs):
        stock = self.get_object()
        return JsonResponse(stock.json())


class VilleDetailView(DetailView):
    model = Ville

    def get(self, request, *args, **kwargs):
        ville = self.get_object()
        return JsonResponse(ville.json())


class QuantiteRessourceDetailView(DetailView):
    model = QuantiteRessource

    def get(self, request, *args, **kwargs):
        quantite = self.get_object()
        return JsonResponse(quantite.json())


class EtapeDetailView(DetailView):
    model = Etape

    def get(self, request, *args, **kwargs):
        etape = self.get_object()
        return JsonResponse(etape.json())


class ProduitDetailView(DetailView):
    model = Produit

    def get(self, request, *args, **kwargs):
        produit = self.get_object()
        return JsonResponse(produit.json())


class SiegeSocialDetailView(DetailView):
    model = SiegeSocial

    def get(self, request, *args, **kwargs):
        siege = self.get_object()
        return JsonResponse(siege.json())
