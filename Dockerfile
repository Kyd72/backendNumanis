# Utiliser une image de base pour Python
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installer les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source dans le conteneur
COPY . /app/

# Exposer le port sur lequel Django s'exécute
EXPOSE 8000


# Collecter les fichiers statiques de Django
RUN python manage.py collectstatic --noinput

# Configuration de l'environnement de production
ENV DJANGO_SETTINGS_MODULE=nom_de_votre_projet.settings.production
ENV PYTHONPATH=/app

# Exécuter les migrations au démarrage du conteneur
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
