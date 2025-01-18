#include <cpr/cpr.h>

#include <iostream>
#include <memory>
#include <nlohmann/json.hpp>
#include <string>

using namespace std;
using json = nlohmann::json;

/////////////////////////////////////////////////////////////////////////////////////
// Classe Ville
class Ville {
 public:
  // Attributs
  string Nom;
  int CodePostal;
  int Prix_m2;
  // Constructeur avec paramètres
  Ville(string nom, int cp, int prix) {
    Nom = nom;
    CodePostal = cp;
    Prix_m2 = prix;
  }
  // Constructeur json
  Ville(const json& j) {
    try {
      Nom = j.at("nom").get<string>();
      CodePostal = j.at("code_postal").get<int>();
      Prix_m2 = j.at("prix_m2").get<int>();
    } catch (const nlohmann::json::exception& e) {
      cerr << "Erreur lors du parsing du JSON : " << e.what() << endl;
      throw;  // Repropage l'exception pour une gestion plus haut
    }
  }

 public:
  json to_json() const {
    return {{"nom", Nom}, {"code_postal", CodePostal}, {"prix_m2", Prix_m2}};
  }
  // Methode Affichage
  void Affichage() {
    cout << "Nom de la ville est : " << Nom << endl;
    cout << "Le code postal est : " << CodePostal << endl;
    cout << "Le prix par m2 est : " << Prix_m2 << endl;
  }
};
/////////////////////////////////////////////////////////////////////////////////////
// Classe Local
class Local {
 public:
  string nom;
  int surface;
  shared_ptr<Ville> ville;  // Pointeur unique

  // Constructeur
  Local(const string& n, shared_ptr<Ville> v, int s)
      : nom(n),
        ville(std::move(v)),
        surface(s) {}  // Use std::move to transfer ownership of Ville
  virtual int cost() const = 0;
  // Destructeur virtuel
  virtual ~Local() = default;

  // Calcul de cout (méthode virtuelle pure)
  virtual int getCost() const = 0;
};
/////////////////////////////////////////////////////////////////////////////////////
// Classe SiegeSocial
class SiegeSocial : public Local {
 public:
  SiegeSocial(string nom, shared_ptr<Ville> v, int surface)
      : Local(nom, std::move(v), surface) {}

  int cost() const override {
    // Assuming a cost based on Ville's Prix_m2
    return ville->Prix_m2 * surface;
  }

  json to_json() const {
    return {{"nom", nom}, {"ville", ville->to_json()}, {"surface", surface}};
  }
};
/////////////////////////////////////////////////////////////////////////////////////
// Classe Machine
class Machine {
 public:
  string Nom;
  int Prix;
  string n_serie;

  int cost() const { return Prix; }

  Machine(std::string n, int p, std::string n_s)
      : Nom(n), Prix(p), n_serie(n_s) {}

  // Constructeur json
  Machine(const json& j) {
    try {
      Nom = j.at("nom").get<string>();
      Prix = j.at("prix").get<int>();
      n_serie = j.at("n_serie").get<string>();
    } catch (const nlohmann::json::exception& e) {
      cerr << "Erreur lors du parsing du JSON : " << e.what() << endl;
      throw;  // Repropage l'exception pour une gestion plus haut
    }
  }

  void Affichage() {
    cout << "Nom de la machine est : " << Nom << endl;
    cout << "Le prix est : " << Prix << endl;
    cout << "Le numéro série est : " << n_serie << endl;
  }
  json to_json() const {
    return {{"nom", Nom}, {"prix", Prix}, {"n_serie", n_serie}};
  }
};

/////////////////////////////////////////////////////////////////////////////////////
// Classe Usine
class Usine : public Local {
 public:
  vector<shared_ptr<Machine>> Machines;

  Usine(string nom, shared_ptr<Ville> v, int surface)
      : Local(nom, std::move(v), surface) {}

  void add_machine(shared_ptr<Machine> machine) { Machines.push_back(machine); }

  int cost() const override {
    int total_cost = ville->Prix_m2 * surface;
    for (const auto& machine : Machines) {
      total_cost += machine->cost();
    }
    return total_cost;
  }

  json to_json() const {
    json machines_json = json::array();
    for (const auto& machine : Machines) {
      machines_json.push_back(machine->to_json());
    }
    return {{"nom", nom},
            {"ville", ville->to_json()},
            {"surface", surface},
            {"machines", machines_json}};
  }
};
/////////////////////////////////////////////////////////////////////////////////////
// Classe Objet
class Objet {
 public:
  string Nom;
  int Prix;

  Objet(string nom, int prix) : Nom(nom), Prix(prix) {}

  virtual ~Objet() = default;

  // Méthode virtuelle pour calculer le coût
  virtual int cost() const = 0;

  virtual json to_json() const { return {{"nom", Nom}, {"prix", Prix}}; }
};
/////////////////////////////////////////////////////////////////////////////////////
// Class Ressource
class Ressource : public Objet {
 public:
  string Nom;
  int Prix;

  Ressource(string nom, int prix) : Objet(nom, prix) {}

  json to_json() const { return {{"nom", Nom}, {"prix", Prix}}; }
};
/////////////////////////////////////////////////////////////////////////////////////
// Classe QuantiteRessource
class QuantiteRessource {
 public:
  shared_ptr<Ressource> RessourceObj;
  int Quantite;

  QuantiteRessource(shared_ptr<Ressource> res, int quantite)
      : RessourceObj(std::move(res)),
        Quantite(quantite) {}  // Use std::move for RessourceObj

  int cost() const { return RessourceObj->Prix * Quantite; }

  json to_json() const {
    return {{"ressource", RessourceObj->to_json()}, {"quantite", Quantite}};
  }
};
/////////////////////////////////////////////////////////////////////////////////////
// Classe Etape
class Etape {
 public:
  string Nom;
  shared_ptr<Machine> MachineObj;
  shared_ptr<QuantiteRessource> QuantiteRessourceObj;
  int Duree;

  Etape(string nom, shared_ptr<Machine> machine,
        shared_ptr<QuantiteRessource> ressource, int duree)
      : Nom(nom),
        MachineObj(std::move(machine)),
        QuantiteRessourceObj(std::move(ressource)),
        Duree(duree) {}

  json to_json() const {
    return {{"nom", Nom},
            {"machine", MachineObj->to_json()},
            {"quantite_ressource", QuantiteRessourceObj->to_json()},
            {"duree", Duree}};
  }
};
/////////////////////////////////////////////////////////////////////////////////////
// Classe Produit
class Produit : public Objet {
 public:
  string Nom;
  shared_ptr<Etape> PremiereEtape;

  Produit(string nom, shared_ptr<Etape> etape)
      : Objet(nom, 0), PremiereEtape(std::move(etape)) {}

  json to_json() const {
    return {{"nom", Nom}, {"premiere_etape", PremiereEtape->to_json()}};
  }
};
/////////////////////////////////////////////////////////////////////////////////////
// Classe Stock
class Stock {
 public:
  shared_ptr<Ressource> RessourceObj;
  int Quantite;
  shared_ptr<Usine> UsineObj;

  Stock(shared_ptr<Ressource> ressource, int quantite, shared_ptr<Usine> usine)
      : RessourceObj(std::move(ressource)),
        Quantite(quantite),
        UsineObj(std::move(usine)) {}

  // Méthode pour calculer le coût total des ressources en stock
  int cost() const { return RessourceObj->Prix * Quantite; }

  // Méthode JSON
  json to_json() const {
    return {{"ressource", RessourceObj->to_json()},
            {"quantite", Quantite},
            {"usine", UsineObj->to_json()}};
  }
};

/////////////////////////////////////////////////////////////////////////////////////

int main() {
  // Création d'objet
  Ville Toulouse("Paris", 75000, 2000);
  Toulouse.Affichage();

  /*  Parsing Ville */
  cpr::Response r = cpr::Get(
      cpr::Url{"http://localhost:8000/Ville/2"});  // Récupération des données
  cout << endl << r.status_code << endl;
  cout << r.header["content-type"] << endl;
  cout << endl << r.text << endl;

  cout << endl << "Parser le texte" << endl;
  json data = json::parse(r.text);
  cout << data << endl;

  Ville jsTLS(data);
  jsTLS.Affichage();

  /*  Parsing Machines */
  cpr::Response r2 = cpr::Get(
      cpr::Url{"http://localhost:8000/Machine/1"});  // Récupération des données
  cout << endl << r2.status_code << endl;
  cout << r2.header["content-type"] << endl;
  cout << endl << r2.text << endl;

  cout << endl << "Parser le texte" << endl;
  json data2 = json::parse(r2.text);
  cout << data2 << endl;

  // Machine jsPerceuse(data2);
  // jsPerceuse.Affichage();

  /*  Parsing Usine */
  cpr::Response r3 = cpr::Get(
      cpr::Url{"http://localhost:8000/Usine/1"});  // Récupération des données
  cout << endl << r3.status_code << endl;
  cout << r3.header["content-type"] << endl;
  cout << endl << r3.text << endl;

  cout << endl << "Parser le texte" << endl;
  json data3 = json::parse(r3.text);
  cout << data3 << endl;

  /*  Parsing Siege Social */
  cpr::Response r4 = cpr::Get(cpr::Url{
      "http://localhost:8000/SiegeSocial/1"});  // Récupération des données
  cout << endl << r4.status_code << endl;
  cout << r4.header["content-type"] << endl;
  cout << endl << r4.text << endl;

  cout << endl << "Parser le texte" << endl;
  json data4 = json::parse(r4.text);
  cout << data4 << endl;

  /*  Parsing Stock */
  cpr::Response r5 = cpr::Get(
      cpr::Url{"http://localhost:8000/Stock/1"});  // Récupération des données
  cout << endl << r5.status_code << endl;
  cout << r5.header["content-type"] << endl;
  cout << endl << r5.text << endl;

  cout << endl << "Parser le texte" << endl;
  json data5 = json::parse(r5.text);
  cout << data5 << endl;

  /*  Parsing Etape */
  cpr::Response r6 = cpr::Get(
      cpr::Url{"http://localhost:8000/Etape/1"});  // Récupération des données
  cout << endl << r6.status_code << endl;
  cout << r6.header["content-type"] << endl;
  cout << endl << r6.text << endl;

  cout << endl << "Parser le texte" << endl;
  json data6 = json::parse(r6.text);
  cout << data6 << endl;

  /*  Parsing Ressource */
  cpr::Response r7 = cpr::Get(cpr::Url{
      "http://localhost:8000/Ressource/1"});  // Récupération des données
  cout << endl << r7.status_code << endl;
  cout << r7.header["content-type"] << endl;
  cout << endl << r7.text << endl;

  cout << endl << "Parser le texte" << endl;
  json data7 = json::parse(r7.text);
  cout << data7 << endl;
  /*  Parsing Quantite Ressource */
  cpr::Response r8 = cpr::Get(
      cpr::Url{"http://localhost:8000/QuantiteRessource/1"});  // Récupération
                                                               // des données
  cout << endl << r8.status_code << endl;
  cout << r8.header["content-type"] << endl;
  cout << endl << r8.text << endl;

  cout << endl << "Parser le texte" << endl;
  json data8 = json::parse(r3.text);
  cout << data8 << endl;

  /*  Parsing Produit */
  cpr::Response r9 = cpr::Get(
      cpr::Url{"http://localhost:8000/Produit/1"});  // Récupération des données
  cout << endl << r9.status_code << endl;
  cout << r9.header["content-type"] << endl;
  cout << endl << r9.text << endl;

  cout << endl << "Parser le texte" << endl;
  json data9 = json::parse(r9.text);
  cout << data9 << endl;

  return 0;
}
