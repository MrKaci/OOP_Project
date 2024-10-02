#include <iostream>
#include <string>

using namespace std;

class Ville {
 public:
  // Attributs
  string Nom;
  int CodePostal;
  int Prix_m2;
  // Constructeur
  Ville(string nom, int cp, int prix) {
    Nom = nom;
    CodePostal = cp;
    Prix_m2 = prix;
  }

 public:
  // Méthode Affichage
  void Affichage() {
    cout << "Nom de la ville est : " << Nom << endl;
    cout << "Le code postal est : " << CodePostal << endl;
    cout << "Le prix par m2 est : " << Prix_m2 << endl;
  }
};

int main() {
  Ville Toulouse("Paris", 75000, 2000);
  Toulouse.Affichage();

  return 0;
}
