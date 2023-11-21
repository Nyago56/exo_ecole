# Utilisez une image Python officielle en tant qu'image parent
FROM python:3.9-slim-bullseye

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le script Python dans le conteneur
COPY main.py /app/

# Commande à exécuter lors du démarrage du conteneur
CMD ["python", "main.py"]
