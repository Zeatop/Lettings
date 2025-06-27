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

Créez un superuser:

.. code-block:: bash

   python manage.py createsuperuser

Accédez au panel d'administration à l'adresse : http://localhost:8000/admin

* **Utilisateur :** votreIDAdmin
* **Mot de passe :** votreMDPAdmin