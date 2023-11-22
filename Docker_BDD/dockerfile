# Utilisez une image Python officielle en tant qu'image parent
FROM python:3.9-slim-bullseye

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le script Python dans le conteneur
COPY com_bdd.py /app/

# Commande à exécuter lors du démarrage du conteneur
CMD ["python", "com_bdd.py"]
#Ajout de la bibliothèque au container
RUN pip install mysql-connector-python
