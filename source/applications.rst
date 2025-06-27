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

.. automodule:: lettings.models
   :members:
   :undoc-members:
   :show-inheritance:

* ``Address`` : Adresse physique (numéro, rue, ville, état, code postal, pays)
* ``Letting`` : Location avec titre et adresse associée

**Vues :**

.. automodule:: lettings.views
   :members:
   :undoc-members:
   :show-inheritance:

* ``lettings_index`` : Liste de toutes les locations
* ``letting`` : Détail d'une location spécifique

**URLs :**

.. automodule:: lettings.urls
   :members:
   :undoc-members:
   :show-inheritance:

* ``/lettings/`` : Index des locations
* ``/lettings/<letting_id>/`` : Détail d'une location

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

* ``Profile`` : Profil utilisateur avec ville favorite

**Vues :**

.. automodule:: profiles.views
   :members:
   :undoc-members:
   :show-inheritance:

* ``profiles_index`` : Liste de tous les profils
* ``profile`` : Détail d'un profil spécifique

**URLs :**

.. automodule:: profiles.urls
   :members:
   :undoc-members:
   :show-inheritance:

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