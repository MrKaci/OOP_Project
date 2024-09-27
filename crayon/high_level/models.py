# Create your models here.
from django.db import models
import json


##########################################################################################
class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField()
    prix_m2 = models.IntegerField()

    # Méthode Calcul cout
    def costs(self):
        return self.prix_m2

    def __str__(self):
        return f"{self.nom} {self.code_postal} {self.prix_m2}"

    # Méthode JSON
    def json(self):
        return {
            "nom": self.nom,
            "code_postal": self.code_postal,
            "prix_m2": self.prix_m2,
        }


##########################################################################################
# Classe Abstraite
class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    surface = models.IntegerField()

    # Méthode Calcul cout
    def costs(self):
        return self.surface

    class Meta:
        abstract = True


##########################################################################################
class SiegeSocial(Local):
    pass

    # Méthode JSON
    def json(self):
        return json.dumps(
            {
                "nom": self.nom,
                "prix": self.ville,
                "surface": self.surface,
            }
        )


##########################################################################################
class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    n_serie = models.CharField(max_length=100)

    # Méthode Calcul cout
    def costs(self):
        return self.prix

    # Méthode str
    def __str__(self):
        return f"{self.nom} {self.prix} {self.n_serie}"

    # Méthode JSON
    def json(self):
        return json.dumps(
            {
                "nom": self.nom,
                "n_serie": self.n_serie,
                "prix": self.prix,
            }
        )


##########################################################################################
class Usine(Local):
    machines = models.ManyToManyField(Machine)

    # Méthode Calcul cout
    def costs(self):
        TotCost = 0
        CostMach = 0
        CostRess = 0

        for machine in self.machines.all():
            CostMach = CostMach + machine.prix
        print(CostMach)

        for stock in self.stock_set.all():
            CostRess += stock.nombre * stock.ressource.prix
        print(CostRess)

        print(self.ville.prix_m2 * self.surface)
        TotCost = CostMach + CostRess + self.ville.prix_m2 * self.surface

        return TotCost

    # Méthode JSON
    def json(self):
        list = []
        for machines in self.machines.all():
            list.append(machines.id)
        return {"machines.id": list}


##########################################################################################
#  Classe Abstraite
class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()

    class Meta:
        abstract = True


##########################################################################################
class Ressource(Objet):
    pass

    # Méthode JSON
    def json(self):
        return json.dumps(
            {
                "nom": self.nom,
                "prix": self.prix,
            }
        )


##########################################################################################
class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    # Méthode Calcul cout
    def costs(self):
        return self.quantite

    # Méthode str
    def __str__(self):
        return f"{self.ressource} {self.quantite}"

    # Méthode JSON
    def json(self):
        return json.dumps(
            {
                "quantite": self.quantite,
                "id": self.ressource.id,
            }
        )


##########################################################################################
class Etape(models.Model):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    quantite_ressource = models.ForeignKey(QuantiteRessource, on_delete=models.CASCADE)
    duree = models.IntegerField()
    etape_suivante = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.CASCADE
    )

    # Méthode str
    def __str__(self):
        return f"{self.nom} {self.duree} {self.quantite_ressource} {self.etape_suivante} {self.machine}"

    # Méthode JSON
    def json(self):
        return json.dumps(
            {
                "nom": self.nom,
                "duree": self.duree,
                "id1": self.machine.id,
                "id2": self.quantite_ressource.id,
                "id3": self.etape_suivante.id,
            }
        )


##########################################################################################
class Produit(Objet):
    premiere_etape = models.ForeignKey(Etape, on_delete=models.CASCADE)

    # Méthode str
    def __str__(self):
        return f"{self.premiere_etape}"

    # Méthode JSON
    def json(self):
        return json.dumps(
            {
                "premiere etape id": self.premiere_etape.id,
            }
        )


##########################################################################################
class Stock(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    nombre = models.IntegerField()
    usine = models.ForeignKey(Usine, on_delete=models.CASCADE)

    # Méthode Calcul cout
    def costs(self):
        return self.nombre

    # Méthode str
    def __str__(self):
        return f"{self.ressource} {self.nombre}"

    # Méthode JSON
    def json(self):
        return json.dumps(
            {
                "nombre": self.nombre,
                "id1": self.ressource.id,
                "id2": self.usine.id,
            }
        )
