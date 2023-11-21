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
3. Build le container dans une invite de commande
```
docker build -t dockerbg .
```
4. Lancer le container dans l'invite de commande
```
docker run dockerbg
```
- Vérification de l'état du conteneur :

```
docker ps -a
```
- Voir l'id du docker :

```
docker run -d dockerbg
```
## Code python
```
import time

i = 0
print("Début")


while True:
    try:
        i = i + 1
        for o in range(i):
            print("CIAO", end='', flush=True)
        time.sleep(1)
        print(" ")
    except KeyboardInterrupt as Exc:
        repr(Exc)
        break

    
    
print("Fin")
```
