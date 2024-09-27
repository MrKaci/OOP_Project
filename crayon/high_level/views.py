# Create your views here.
from django.views.generic import DetailView
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
from django.http import JsonResponse


class MachineDetailView(DetailView):
    model = Machine

    def render_to_response(self, arg, **response_kwargs):
        return JsonResponse(self.object.json())


class UsineDetailView(DetailView):
    model = Usine

    def render_to_response(self, arg, **response_kwargs):
        return JsonResponse(self.object.json())


class RessourceDetailView(DetailView):
    model = Ressource

    def render_to_response(self, arg, **response_kwargs):
        return JsonResponse(self.object.json())


class StockDetailView(DetailView):
    model = Stock

    def render_to_response(self, *arg, **response_kwargs):
        return JsonResponse(self.object.json())


class VilleDetailView(DetailView):
    model = Ville

    def render_to_response(self, arg, **response_kwargs):
        return JsonResponse(self.object.json())


class QuantiteRessourceDetailView(DetailView):
    model = QuantiteRessource

    def render_to_response(self, arg, **response_kwargs):
        return JsonResponse(self.object.json())


class EtapeDetailView(DetailView):
    model = Etape

    def render_to_response(self, arg, **response_kwargs):
        return JsonResponse(self.object.json())


class ProduitDetailView(DetailView):
    model = Produit

    def render_to_response(self, arg, **response_kwargs):
        return JsonResponse(self.object.json())


class SiegeSocialDetailView(DetailView):
    model = SiegeSocial

    def render_to_response(self, arg, **response_kwargs):
        return JsonResponse(self.object.json())
