#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>
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
  // Création d'objet
  Ville Toulouse("Paris", 75000, 2000);
  Toulouse.Affichage();

  // Récupération des données
  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/Ville/1"});

  cout << r.status_code << endl;             // 200
  cout << r.header["content-type"] << endl;  // application/json; charset=utf-8
  cout << r.text << endl;                    // JSON text string

  return 0;
}
