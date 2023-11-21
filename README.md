# exo_ecole
## Cour docker

**Image exemple :**

> odoo / mysql /adminer

**Voir Image :**

> docker images

**Ajout d'une image :**

> docker pull "nom image"

**Suprimer une image :**

> docker rmi "nom image"

**run un container :**

> docker run "nom container"

**stop un container :**

> docker stop "nom container"

**supprimer un container :**

> docker rm "nom container"

** Code Python dans un container :**

1. Créer un fichier "dockerfile" (pas de .quelquechose) dans le même dossier que le code python
2. Copier le code suivant dans le fichier "dockerfile" :

```python# Utilisez une image Python officielle en tant qu'image parent
FROM python:3.9-slim-bullseye

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le script Python dans le conteneur
COPY main.py /app/

# Commande à exécuter lors du démarrage du conteneur
CMD ["python", "main.py"]
```

> docker run "nom container"


## création d'un code python infini


## mise dans un docker du code + lancement
