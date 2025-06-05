Installation
============

Prérequis
---------

- Python 3.6+
- pip
- Git

Étapes d'installation
---------------------

1. **Cloner le repository**

   .. code-block:: bash

      git clone https://github.com/[username]/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

2. **Créer un environnement virtuel**

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # Linux/Mac
      # ou
      venv\Scripts\activate     # Windows

3. **Installer les dépendances**

   .. code-block:: bash

      pip install -r requirements.txt

4. **Migrations**

   .. code-block:: bash

      python manage.py migrate

5. **Lancer le serveur**

   .. code-block:: bash

      python manage.py runserver

L'application sera accessible sur http://127.0.0.1:8000/ 