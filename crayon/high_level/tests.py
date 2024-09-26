# Create your tests here.
from django.test import TestCase
from .models import Machine, Usine, Ressource, Stock, Ville


#   Test de modèle machine
# class MachineModelTests(TestCase):
#    def test_machine_creation(self):
#        self.assertEqual(Machine.objects.count(), 0)
#        Machine.objects.create(nom="scie", prix=1_000, n_serie="1683AI2")
#        self.assertEqual(Machine.objects.count(), 1)


#   Test de calcul de cout
class CalculCoutTests(TestCase):
    def test_calcul_cout(self):
        V = Ville.objects.create(nom="Labège", code_postal=31400, prix_m2=2000)
        U = Usine.objects.create(nom="Thanina Company", ville=V, surface=50)
        m1 = Machine.objects.create(prix=1000)
        m2 = Machine.objects.create(prix=2000)
        U.machines.add(m1)
        U.machines.add(m2)
        r1 = Ressource.objects.create(nom="bois", prix=10)
        Stock.objects.create(ressource=r1, nombre=1000, usine=U)
        r2 = Ressource.objects.create(nom="mine", prix=15)
        Stock.objects.create(ressource=r2, nombre=50, usine=U)

        # a = Usine.objects.first()
        print(U.costs())
