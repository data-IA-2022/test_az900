# Création d'une image dans un coteneur sur Azure (déploiement)

## Build une image avec un dockerfile :

docker build -t #<nom de l'image># .

## Run de l'image :

docker run -p 5000:5000 #<nom de l'image>#

## Voir les images dans docker : 

docker images => voir les images sur le système


Une fois l'image fonctionnelle en local, l'on peux créer un registre de container (container registry) et ensuite créer des instances de conteneur qui réutilise l'image installer dans le container registry. Il est même possible de créer plusieurs instances de cette image.

documentation : https://learn.microsoft.com/fr-fr/azure/container-registry/container-registry-get-started-docker-cli?tabs=azure-cli

### Etape 1 : Création sur azure d'un container registry

rechercher dans la barre de recherche sur azure pour créer un container registry (registre de conteneur)

### Etape 2 : Connexion a un registre de container distant 

docker login <nom du registre>.azurecr.io   ( ou az acr login -n <nom du registre>)

### Etape 3 : Vérifier le nom de l'image et la retag avec 

docker tag <nom de l'image>:<tag> <nom du registre>.azurecr.io/<nom de l'image>:<tag>
docker tag flask-app:latest registredepartement.azurecr.io/flask-app:latest

### Etape 4 : push l'image

docker push <nom du registre>.azurecr.io/<nom de l'image>:<tag>

### Etape 5 : Création sur Azure d'une instance de container 

avec comme source le registre (faire la recherche dans la barre de recherche instance de container)


### Résolution d'un problème d'author avec git 

git config --global user.email "jeremy.mikaleff@gmail.com"
git config --global user.name "JeremyMikaleff"