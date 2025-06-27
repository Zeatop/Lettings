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