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