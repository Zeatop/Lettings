.. Lettings documentation master file, created by
   sphinx-quickstart on Sat Jun 14 10:33:04 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Orange County Lettings Documentation
====================================

Bienvenue dans la documentation du site web Orange County Lettings, une plateforme de gestion de locations de vacances.

.. contents:: Table des matières
   :local:
   :depth: 2

Vue d'ensemble
==============

Orange County Lettings est une application web Django dédiée à la gestion de locations de vacances. Le site permet de consulter des profils d'utilisateurs et des annonces de locations.

**Fonctionnalités principales :**

* Gestion des profils utilisateurs
* Catalogue des locations disponibles
* Interface d'administration Django
* API REST pour l'accès aux données
* Monitoring des erreurs avec Sentry
* Déploiement automatisé sur Render

**Technologies utilisées :**

* Django 3.0
* SQLite (base de données)
* Bootstrap (interface utilisateur)
* Sentry (monitoring)
* Docker (containerisation)
* GitHub Actions (CI/CD)
* Render (hébergement)

Installation et développement local
===================================

Prérequis
---------

* Python 3.6 ou supérieur
* Git CLI
* SQLite3 CLI
* Compte GitHub avec accès au repository

Configuration de l'environnement
---------------------------------

**1. Cloner le repository :**

.. code-block:: bash

   git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

**2. Créer l'environnement virtuel :**

.. code-block:: bash

   python -m venv venv
   
   # Sur macOS/Linux
   source venv/bin/activate
   
   # Sur Windows
   .\venv\Scripts\Activate.ps1

**3. Installer les dépendances :**

.. code-block:: bash

   pip install --requirement requirements.txt

**4. Lancer le serveur de développement :**

.. code-block:: bash

   python manage.py runserver

Le site sera accessible à l'adresse : http://localhost:8000

Panel d'administration
----------------------

Accédez au panel d'administration à l'adresse : http://localhost:8000/admin

* **Utilisateur :** admin
* **Mot de passe :** Abc1234!

Architecture du projet
======================

Structure des dossiers
-----------------------

.. code-block:: text

   oc_lettings_site/
   ├── lettings/              # Application gestion des locations
   ├── profiles/              # Application gestion des profils
   ├── oc_lettings_site/      # Configuration principale Django
   ├── templates/             # Templates HTML
   ├── static/                # Fichiers statiques (CSS, JS, images)
   ├── requirements.txt       # Dépendances Python
   ├── Dockerfile            # Configuration Docker
   ├── .github/workflows/    # CI/CD GitHub Actions
   └── manage.py             # Script de gestion Django

Configuration principale
-------------------------

Le fichier ``oc_lettings_site/settings.py`` contient la configuration principale :

* **Base de données :** SQLite (``oc-lettings-site.sqlite3``)
* **Applications installées :** lettings, profiles, admin Django
* **Middleware :** sécurité, sessions, authentification, WhiteNoise
* **Templates :** répertoire ``templates/`` avec Bootstrap
* **Fichiers statiques :** gérés par WhiteNoise
* **Monitoring :** intégration Sentry SDK

Applications Django
===================

Application Lettings
--------------------

**Modèles :**

* ``Address`` : Adresse physique (numéro, rue, ville, état, code postal, pays)
* ``Letting`` : Location avec titre et adresse associée

**Vues :**

* ``lettings_index`` : Liste de toutes les locations
* ``letting`` : Détail d'une location spécifique

**URLs :**

* ``/lettings/`` : Index des locations
* ``/lettings/<letting_id>/`` : Détail d'une location

**Templates :**

* ``lettings_index.html`` : Liste des locations
* ``letting.html`` : Détail d'une location

Application Profiles
--------------------

**Modèles :**

* ``Profile`` : Profil utilisateur avec ville favorite

**Vues :**

* ``profiles_index`` : Liste de tous les profils
* ``profile`` : Détail d'un profil spécifique

**URLs :**

* ``/profiles/`` : Index des profils
* ``/profiles/<username>/`` : Détail d'un profil

**Templates :**

* ``profiles_index.html`` : Liste des profils
* ``profile.html`` : Détail d'un profil

Base de données
===============

Modèle de données
-----------------

**Table Address :**

* ``id`` : Clé primaire auto-incrémentée
* ``number`` : Numéro de rue (entier positif, max 9999)
* ``street`` : Nom de rue (max 64 caractères)
* ``city`` : Ville (max 64 caractères)
* ``state`` : État (2 caractères)
* ``zip_code`` : Code postal (entier positif, max 99999)
* ``country_iso_code`` : Code pays ISO (3 caractères)

**Table Letting :**

* ``id`` : Clé primaire auto-incrémentée
* ``title`` : Titre de la location (max 256 caractères)
* ``address_id`` : Clé étrangère vers Address (OneToOne)

**Table Profile :**

* ``id`` : Clé primaire auto-incrémentée
* ``user_id`` : Clé étrangère vers User Django (OneToOne)
* ``favorite_city`` : Ville favorite (max 64 caractères, optionnel)

Migrations
----------

Le projet utilise un système de migrations pour séparer les modèles de l'application principale vers les applications spécialisées :

* ``lettings/migrations/0001_initial.py`` : Migration des modèles Address et Letting
* ``profiles/migrations/0001_initial.py`` : Migration du modèle Profile
* ``oc_lettings_site/migrations/0003_auto_20250606_1405.py`` : Suppression des anciens modèles

Commandes utiles
----------------

.. code-block:: bash

   # Accéder à la base de données SQLite
   sqlite3 oc-lettings-site.sqlite3
   
   # Voir les tables
   .tables
   
   # Voir la structure d'une table
   pragma table_info(lettings_address);
   
   # Requête d'exemple
   select user_id, favorite_city from profiles_profile where favorite_city like 'B%';

Déploiement
===========

Architecture de déploiement
----------------------------

Le projet utilise une pipeline CI/CD avec GitHub Actions pour automatiser le déploiement :

**1. Build et tests (ubuntu-22.04) :**

* Checkout du code source
* Construction de l'image Docker
* Exécution des tests avec coverage
* Push de l'image vers Docker Hub

**2. Déploiement sur Render :**

* Déclenchement automatique après succès des tests
* Déploiement via API Render

Configuration Docker
---------------------

**Dockerfile :**

* Image de base : ``python:3.12-alpine``
* Installation des dépendances via ``requirements.txt``
* Exposition du port 8000
* Point d'entrée : ``entrypoint.sh``
* Serveur ASGI : Daphne

**Variables d'environnement :**

* ``PYTHONDONTWRITEBYTECODE=1``
* ``PYTHONUNBUFFERED=1``
* ``GIT_COMMIT`` : Hash du commit (build arg)

Script de déploiement
---------------------

Le fichier ``entrypoint.sh`` prépare l'application :

.. code-block:: bash

   #!/bin/sh
   python manage.py migrate --noinput
   python manage.py collectstatic --noinput
   exec "$@"

**Secrets GitHub requis :**

* ``DOCKER_USERNAME`` : Nom d'utilisateur Docker Hub
* ``DOCKER_PASSWD`` : Mot de passe Docker Hub
* ``RENDER_API_KEY`` : Clé API Render
* ``RENDER_SERVICE_ID`` : ID du service Render

Tests
=====

Framework de tests
------------------

Le projet utilise **pytest** avec **pytest-django** pour les tests.

Configuration des tests
------------------------

**Fichier ``setup.cfg`` :**

.. code-block:: ini

   [tool:pytest]
   DJANGO_SETTINGS_MODULE = oc_lettings_site.settings
   python_files = tests.py
   addopts = -v

Exécution des tests
-------------------

.. code-block:: bash

   # Lancer tous les tests
   pytest
   
   # Tests avec coverage
   pytest --cov=.
   
   # Tests d'une application spécifique
   pytest lettings/tests.py
   pytest profiles/tests.py

Tests de l'application Lettings
--------------------------------

**test_lettings_index_view :**

* Vérifie le statut HTTP 200
* Vérifie la présence de ``lettings_list`` dans le contexte

**test_letting_detail_view :**

* Crée une adresse et une location de test
* Vérifie l'affichage correct des détails

Tests de l'application Profiles
--------------------------------

**test_profiles_index_view :**

* Vérifie le statut HTTP 200
* Vérifie la présence de ``profiles_list`` dans le contexte

**test_profile_detail_view :**

* Crée un utilisateur et un profil de test
* Vérifie l'affichage correct du profil

Qualité du code
===============

Linting avec Flake8
--------------------

Configuration dans ``setup.cfg`` :

.. code-block:: ini

   [flake8]
   max-line-length = 99
   exclude = **/migrations/*,env

Commande :

.. code-block:: bash

   flake8

Coverage des tests
------------------

Génération d'un rapport de coverage :

.. code-block:: bash

   pytest --cov=. --cov-report=html

Monitoring et observabilité
============================

Intégration Sentry
-------------------

Le projet utilise **Sentry SDK** pour le monitoring des erreurs et des performances.

**Configuration dans ``settings.py`` :**

.. code-block:: python

   import sentry_sdk
   from sentry_sdk.integrations.django import DjangoIntegration
   
   sentry_sdk.init(
       dsn="https://505a28f623ff3376de2f4092d8515558@o4509147190460416.ingest.de.sentry.io/4509162976182352",
       integrations=[DjangoIntegration()],
       traces_sample_rate=1.0,
       profiles_sample_rate=1.0,
       send_default_pii=True,
       environment="development",
   )

**Fonctionnalités Sentry :**

* Capture automatique des erreurs Django
* Profiling des performances
* Tracking des transactions
* Association des erreurs aux utilisateurs
* Environnements séparés (development/production)

Endpoint de test
----------------

Un endpoint de test est disponible pour vérifier l'intégration Sentry :

.. code-block:: python

   # URL : /sentry-debug/
   def trigger_error(request):
       return 1 / 0

API et endpoints
================

URLs principales
----------------

**Application principale :**

* ``/`` : Page d'accueil (``index``)
* ``/admin/`` : Interface d'administration Django
* ``/sentry-debug/`` : Test de monitoring Sentry

**Application Lettings :**

* ``/lettings/`` : Liste des locations (``lettings_index``)
* ``/lettings/<int:letting_id>/`` : Détail d'une location (``letting``)

**Application Profiles :**

* ``/profiles/`` : Liste des profils (``profiles_index``)
* ``/profiles/<str:username>/`` : Détail d'un profil (``profile``)

Réponses API
------------

**Format de réponse standard :**

* **Content-Type :** ``text/html``
* **Status codes :** 200 (succès), 404 (non trouvé)
* **Templates :** Rendu via le système de templates Django

**Contexte des vues :**

* ``lettings_index`` : ``{'lettings_list': queryset}``
* ``letting`` : ``{'title': string, 'address': object}``
* ``profiles_index`` : ``{'profiles_list': queryset}``
* ``profile`` : ``{'profile': object}``

Dépendances
===========

Requirements.txt
-----------------

.. code-block:: text

   django==3.0                # Framework web
   flake8==3.7.0              # Linting
   pytest-django==3.9.0       # Tests
   pytest-cov==6.1.1          # Coverage des tests
   six==1.17.0                # Compatibilité Python 2/3
   distutils-pytest           # Intégration pytest
   sentry-sdk==2.26.1         # Monitoring
   daphne==3.0.0              # Serveur ASGI
   whitenoise==5.3.0          # Gestion des fichiers statiques

Versions et compatibilité
--------------------------

* **Python :** 3.6+
* **Django :** 3.0
* **Base de données :** SQLite 3
* **Serveur :** Daphne (ASGI)
* **Conteneur :** Docker avec Alpine Linux

Contribution et développement
=============================

Workflow de développement
--------------------------

1. **Fork** du repository
2. **Création** d'une branche feature
3. **Développement** avec tests
4. **Linting** avec flake8
5. **Tests** avec pytest
6. **Pull request** vers master
7. **Review** et merge
8. **Déploiement** automatique

Bonnes pratiques
----------------

* Écrire des tests pour toute nouvelle fonctionnalité
* Respecter le style de code (flake8)
* Documenter les nouvelles APIs
* Utiliser des messages de commit explicites
* Tester en local avant de pousser

Standards de code
-----------------

* **Longueur de ligne :** Maximum 99 caractères
* **Format :** PEP 8 pour Python
* **Documentation :** Docstrings pour les fonctions publiques
* **Tests :** Coverage minimum de 80%

Troubleshooting
===============

Problèmes courants
------------------

**Erreur d'import Django :**

.. code-block:: bash

   # Vérifier l'activation de l'environnement virtuel
   which python
   pip install django

**Base de données non trouvée :**

.. code-block:: bash

   python manage.py migrate

**Erreur de permissions (Docker) :**

.. code-block:: bash

   chmod +x entrypoint.sh

**Tests qui échouent :**

.. code-block:: bash

   # Vérifier les dépendances
   pip install -r requirements.txt
   
   # Nettoyer les fichiers de cache
   find . -name "*.pyc" -delete
   find . -name "__pycache__" -delete

Logs et debugging
-----------------

**Logs Django (développement) :**

.. code-block:: python

   # Dans settings.py
   DEBUG = True
   
   # Logs détaillés
   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'handlers': {
           'console': {
               'class': 'logging.StreamHandler',
           },
       },
       'loggers': {
           'django': {
               'handlers': ['console'],
               'level': 'INFO',
           },
       },
   }

**Logs Docker :**

.. code-block:: bash

   # Voir les logs du conteneur
   docker logs <container_id>
   
   # Mode interactif
   docker run -it python-lettings:latest /bin/sh

Support et contact
==================

**Repository GitHub :** https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR

**Documentation technique :** Cette documentation Sphinx

**Issues et bugs :** GitHub Issues du repository

**Monitoring :** Dashboard Sentry pour les erreurs en production

---

*Documentation générée automatiquement le 14 juin 2025*