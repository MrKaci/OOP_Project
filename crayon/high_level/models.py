# Create your models here.
from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField()
    prix_m2 = models.IntegerField()

    def __str__(self):
        return f"{self.nom} {self.code_postal} {self.prix_m2}"


# Classe Abstraite
class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    surface = models.IntegerField()

    class Meta:
        abstract = True


class SiegeSocial(Local):
    pass


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    n_serie = models.CharField(max_length=100)

    # Méthode str
    def __str__(self):
        return f"{self.nom} {self.prix} {self.n_serie}"


class Usine(models.Model):
    machines = models.ManyToManyField(Machine)

    # Méthode str
    def __str__(self):
        return f"{self.machines}"


#  Classe Abstraite
class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()

    class Meta:
        abstract = True


class Ressource(Objet):
    pass


class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    # Méthode str
    def __str__(self):
        return f"{self.ressource} {self.quantite}"


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


class Produit(Objet):
    premiere_etape = models.ForeignKey(Etape, on_delete=models.CASCADE)

    # Méthode str
    def __str__(self):
        return f"{self.premiere_etape}"


class Stock(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    nombre = models.IntegerField()

    # Méthode str
    def __str__(self):
        return f"{self.ressource} {self.nombre}"
