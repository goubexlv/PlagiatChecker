# PlagiatChecker



Ce projet est une application Django préconfigurée pour fonctionner avec Docker, facilitant le déploiement et l’exécution de l’application dans un environnement isolé.

Prérequis

Avant de commencer, assurez-vous d’avoir les outils suivants installés sur votre machine :
	•	Docker
	•	Docker Compose

Structure du projet

.
├── docker-compose.yml       # Configuration Docker Compose
├── Dockerfile               # Dockerfile pour l'image Django
├── requirements.txt         # Dépendances Python
├── manage.py                # Point d'entrée Django
├── <votre_projet>/          # Répertoire contenant les fichiers du projet Django
└── README.md                # Documentation du projet

Installation et utilisation

Étape 1 : Cloner le projet

Clonez ce dépôt sur votre machine locale :

git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>

Étape 2 : Configuration de l’environnement

Créez un fichier .env dans le répertoire principal pour vos variables d’environnement :

SECRET_KEY=changez_cette_valeur
DEBUG=True
DB_NAME=django_db
DB_USER=django_user
DB_PASSWORD=django_password
DB_HOST=db
DB_PORT=5432

Étape 3 : Construire et lancer les conteneurs

Utilisez Docker Compose pour construire et démarrer les conteneurs :

docker-compose up --build

Étape 4 : Exécuter les migrations

Une fois les conteneurs démarrés, appliquez les migrations pour configurer la base de données :

docker exec -it <nom_du_conteneur_web> python manage.py migrate

Étape 5 : Accéder à l’application

L’application sera accessible à l’adresse :

http://localhost:8000

Commandes utiles
	•	Lancer les conteneurs :

docker-compose up


	•	Arrêter les conteneurs :

docker-compose down


	•	Accéder au shell du conteneur web :

docker exec -it <nom_du_conteneur_web> bash


	•	Collecter les fichiers statiques :

docker exec -it <nom_du_conteneur_web> python manage.py collectstatic


