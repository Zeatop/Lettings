.. Lettings documentation master file, created by
   sphinx-quickstart on Sat Jun 14 10:33:04 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Orange County Lettings Documentation
====================================

Bienvenue dans la documentation du site web Orange County Lettings, une plateforme de gestion de locations de vacances.

.. toctree::
   :maxdepth: 2
   :caption: Table des matières:

   installation
   deploiment
   applications
   API
   tests
   monitoring


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
* GitHub Actions (CI/CD)
* Render (hébergement)

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

