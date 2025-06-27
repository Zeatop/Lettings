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

Projet OC_Lettings
===================

**Settings :**

.. automodule:: oc_lettings_site.settings
   :members:
   :undoc-members:

**Vues :**

.. automodule:: oc_lettings_site.views
   :members:
   :undoc-members:
   :show-inheritance:

**URLs :**

.. automodule:: oc_lettings_site.urls
   :members:
   :undoc-members:
   :show-inheritance:

Applications Django
===================

Application Lettings
--------------------

**Modèles :**

.. automodule:: lettings.models
   :members:
   :undoc-members:
   :show-inheritance:

**Vues :**

.. automodule:: lettings.views
   :members:
   :undoc-members:
   :show-inheritance:

**URLs :**

.. automodule:: lettings.urls
   :members:
   :undoc-members:
   :show-inheritance:

**Templates :**

* ``lettings_index.html`` : Liste des locations
* ``letting.html`` : Détail d'une location

Application Profiles
--------------------

**Modèles :**

.. automodule:: profiles.models
   :members:
   :undoc-members:
   :show-inheritance:

**Vues :**

.. automodule:: profiles.views
   :members:
   :undoc-members:
   :show-inheritance:

**URLs :**

.. automodule:: profiles.urls
   :members:
   :undoc-members:
   :show-inheritance:

**Templates :**

* ``profiles_index.html`` : Liste des profils
* ``profile.html`` : Détail d'un profil
