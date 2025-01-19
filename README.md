# Projet M2 ISTR - Usine de fabrication des crayons
## Description générale
Ce projet est une application web développée avec Django pour la gestion d'une base de donnée d'un usine de fabrication de crayons et de ses propriétés (Local, Ressources, Villes, etc). Il est divisé en deux parties principales : la partie Django pour la gestion des modèles et des données, et la partie C++ pour la récupération et l'affichage des données via une API.

Le diagramme UML est le suivant :
![Tux, the Linux mascot](/Images/UML.png)

Auteurs :
* Arezki AIT KACI
* Yacine MAAMIR

Ce projet a été développé sous un environnement Linux qui est **Ubuntu 20.04.6 LTS**.

**Remarque** : Les commandes présentées fonctionnent dans un système d'exploitation de type Linux, pour l'utilisation sur Windows, il est recommandé de télécharger un outil de Github sur ce lien https://desktop.github.com/download/.

## Pré-requis
Les outils suivants sont nécessaires pour le projet. Voici les commandes qui vous permettenet de vérifier leurs versions et s'ils sont bien installés :
- **Git** : `git --version`, utilisé pour cloner les fichiers du projet.
- **Python** : `python -V` (Python 3 recommandé), pour exécuter le projet.
- **Pip** : `python -m pip -V`, pour pouvoir installer des bibliothèques Python.
- **Venv** : `python -m venv`, pour créer un environnement virtuel Python.
- **CMake** : `pip install cmake`

## Installation & Configuration
1. **Cloner le dépôt dans un dossier local**
```
git clone https://github.com/MrKaci/OOP_Project
```
2. **Se mettre dans le fichier crayon**
```
cd crayon/
```
3. **Créer et activer l'environnement virtuel**
```
python3 -m venv .venv
source .venv/bin/activate
```
4. **Installer les packages nécessaires**
```
pip install -U pip
pip install django
```
5. **Modification du projet (Optionnel)**
```
wget https://gitlab.laas.fr/gsaurel/teach\/-/raw/main/.pre-commit-config.yaml
pip install pre-commit
pre-commit install
pre-commit run -a
```

## Utilisation
### 1. Partie Django
1. **Lancer le serveur de développement**  
    Dans un terminal, naviguez vers le dossier `crayon`, puis exécutez les commandes suivantes :

```
cd crayon/
./manage.py makemigrations
./manage.py migrate
```

Créer un utilisateur, avec un mot de passe en lançant cette commande
```
./manage.py createsuperuser
```

Lancer le serveur
```
./manage.py runserver
```

Entrez dans le site en saisissant ce lien dans la barre URL :
```
http://localhost:8000/admin
```
ça devrait afficher la figure suivante :
![Tux, the Linux mascot](/Images/Web.png)

Entrez l'utilisateur et le mot de passe choisi auparavant et vous aurez la fenêtre suivante :
![Tux, the Linux mascot](/Images/DjangoAdmin.png)

2. **Créer et visualiser les modèles**
Pour créer une ville par exemple, il suffit d'appuyer sur add comme affichée dans la figure précédente.

Ensuite, pour visualiser les élements que vous avez crée, il suffit de séléctionner villes et cela va afficher toutes les villes que vous avez crée :
![Tux, the Linux mascot](/Images/Villes.png)

Vous pouvez accéder aux éléments crées (par exemple ville 1) en introduisant ce lien sur la barre URL du navigateur :
```
http://localhost:8000/Ville/1
```

Sachant que le numéro dans la fin de lien représente le ID de ville, usine, etc. Vous pouvez le récupérer directement sur le lien.

Exemple de la ville Lyon de ID 2 :
![Tux, the Linux mascot](/Images/Lyon.png)

Exemple de l'usine Thanina Company de ID 1 :
![Tux, the Linux mascot](/Images/Usine1.png)

Exemple de la machine perceuse de ID 2 :
![Tux, the Linux mascot](/Images/Machine2.png)

Pour le reste des modèles il suffit d'introduire ce lien
```
http://localhost:8000/
```
En rajoutant à la fin :
```
Ville/ID
Etape/ID
Machine/ID
SiegeSocial/ID
Ressource/ID
QuantiteRessource/ID
Stock/ID
SiegeSocial/ID
Usine/ID
Produit/ID
```

Si nous visualisons le siège crée, sa surface et la ville ou il se situe :
![Tux, the Linux mascot](/Images/SiegeSocial.png)



Nous avons mis en place un scénario de test pour vérifier l'implémentation à travers un exemple qui est :
- Une Usine de 50 m²
- Une la Ville Labège à 2 000 €/m²
- Une Machine à 1 000 €, et une autre à 2 000 €
- Un stock 1000 kg de bois à 10 €/kg
- Un stock 50 m de mine à 15 €/m
Nous nous attendons à ce que le coût total est 110 750 €

Nous lançons le test unitaire avec ces commandes :
```
cd crayon/crayon
python3 ./manage.py test
```
![Tux, the Linux mascot](/Images/TEST.png)

Après exécution nous remarquons que le coût n'est pas de 110750 € mais de 100000 € et donc notre test a détécté l'erreur.


### 2. Partie C++
Pour installer les dépendances nécessaires, ncous ouvrons un autre terminal et nous lançons les commandes suivantes (en gardant dans un autre terminal la commande de runserver):
```
cd crayon/crayon/low_level
$ pip install cmake
```
Pour compiler et exécuter :
```
cmake -B /tmp/build -S .
cmake --build /tmp/build
/tmp/build/low_level
```
ça devrait afficher la fenêtre suivante :
![Tux, the Linux mascot](/Images/Cpp1.png)

![Tux, the Linux mascot](/Images/cpp2.png)

![Tux, the Linux mascot](/Images/cpp3.png)
