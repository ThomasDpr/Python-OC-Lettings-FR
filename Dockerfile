FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collecte des statiques files :
RUN python manage.py collectstatic --noinput

# Exposer le port sur lequel l'application s'exécute
EXPOSE 8000

# Commande pour démarrer l'application
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000