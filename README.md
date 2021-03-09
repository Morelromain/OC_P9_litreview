# OC_P9_litreview
Review web app using Django

* [Readme in English](#english)  
* [Readme in French](#français)  

*English*

traduction à faire

*Français*

## Installation et Execution

Version Python : 3.8.3  

- Cloner ce dépôt de code à l'aide de la commande `$ git clone https://github.com/Morelromain/OC_P9_litreview.git`
- Rendez-vous depuis un terminal à la racine du répertoire OC_P9_litreview avec la commande `$ cd ocmovies-api-fr`
- Créer un environnement virtuel pour le projet avec `$ python -m venv env sous windows` ou `$ python3 -m venv env sous macos ou linux.`
- Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate sous macos ou linux.`
- Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`

## Exectution

Démarrer le serveur avec `$ python manage.py runserver`

Pour acceder à l'application : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage admin

Pour acceder à la gestion de base de donnée : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

#### Compte administrateur pré-existant
- Nom d’utilisateur : `Admin1`
- Mot de passe : : `IbraIbra86`

#### Créer un nouveau compte administrateur

`$ python3 manage.py createsuperuser`

#### Gestion de la BDD SQLITE3

__App Utilisateur__  

- `Utilisateurs` pour la gestion des Utilisateurs
- `User follows` pour la gestion d'abonnement des Utilisateurs

Supprimer un `Utilisateurs` supprimera aussi ses `User follows`, `Tickets` et `Reviews`

__App Critique__  

- `Tickets` pour la gestion de demande de Critiques
- `Review` pour la gestion des Critiques

Supprimer un `Tickets` supprimera aussi ses `Reviews`

*[Documentation Django](https://docs.djangoproject.com/fr/3.1/)*