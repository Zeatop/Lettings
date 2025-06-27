Tests
=====

Framework de tests
------------------

Le projet utilise **pytest** avec **pytest-django** pour les tests.


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