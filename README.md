# OC_P9_litreview
Review web app using Django

[Readme in French](#français)  

*English*

traduction à faire

## Installation

Python Version : 3.8.3  

- Clone this repository using :  
`$ git clone https://github.com/Morelromain/OC_P9_litreview.git`

- Move to the OC_P9_litreview root folder with :  
`$ cd ocmovies-api-fr`

- Create a virtual environment for the project with :  
`$ python -m venv env` on windows or `$ python3 -m venv env sous` on macos or linux.

- Install project dependencies with :  
`$ pip install -r requirements.txt`

## Execution

- Activate the virtual environment with :  
`$ env\Scripts\activate` on windows or `$ source env/bin/activate` on macos or linux.

- Run the server with `$ python manage.py runserver`

To access the application : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Admin use

To access database management : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

#### Pre-existing administrator account
- Username : `Admin1`
- Password : : `IbraIbra86`

#### Create a new administrator account

`$ python3 manage.py createsuperuser`

#### SQLITE3 database management

__App Utilisateur__  *(User)*

- `Utilisateurs` for User management
- `User follows` for the management of User subscriptions

Delete one `Utilisateurs` will also remove its `User follows`, `Tickets` and `Reviews`

__App Critique__  *(Reviews)*

- `Tickets` for Reviews request management
- `Reviews` for the management of Reviews

Delete one `Tickets` will also remove its `Reviews`

*[Django Documentation](https://docs.djangoproject.com/fr/3.1/)*

---

<a name="français"></a>*Français*

## Installation

Version Python : 3.8.3  

- Cloner ce dépôt de code à l'aide de la commande :  
`$ git clone https://github.com/Morelromain/OC_P9_litreview.git`

- Rendez-vous depuis un terminal à la racine du répertoire OC_P9_litreview avec la commande :  
`$ cd ocmovies-api-fr`

- Créer un environnement virtuel pour le projet :  
`$ python -m venv env` sous windows ou `$ python3 -m venv env sous` macos ou linux.

- Installez les dépendances du projet avec la commande :  
`$ pip install -r requirements.txt`

## Exécution

- Activez l'environnement virtuel :  
`$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.`

- Démarrer le serveur avec `$ python manage.py runserver`

Pour accéder à l'application : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage admin

Pour accéder à la gestion de base de donnée : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

#### Compte administrateur pré-existant
- Nom d’utilisateur : `Admin1`
- Mot de passe : : `IbraIbra86`

#### Créer un nouveau compte administrateur

`$ python3 manage.py createsuperuser`

#### Gestion de la base de données SQLITE3

__App Utilisateur__  

- `Utilisateurs` pour la gestion des Utilisateurs
- `User follows` pour la gestion d'abonnement des Utilisateurs

Supprimer un `Utilisateurs` supprimera aussi ses `User follows`, `Tickets` et `Reviews`

__App Critique__  

- `Tickets` pour la gestion de demande de Critiques
- `Reviews` pour la gestion des Critiques

Supprimer un `Tickets` supprimera aussi ses `Reviews`

*[Documentation Django](https://docs.djangoproject.com/fr/3.1/)*