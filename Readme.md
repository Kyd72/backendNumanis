# LISIO-NUMANIS

Le défi: Compression d’images et de vidéos, saurez-vous relever le défi ? A vous de jouer !


## Attendus


L’API aura en entrée l’URL d’une image ou d’une vidéo ainsi que le poids maximal désiré de la nouvelle ressource compressée.

L’API aura en sortie l’URL de la nouvelle ressource compressée ainsi que les données suivantes : le poids de la ressource d'entrée, 
le poids de la ressource de sortie, les dimensions de la ressource d'entrée, les dimensions de la ressource de sortie, le format de
la ressource d'entrée, le format de la ressource de sortie.

Les images d’entrées pourront être dans tous les formats possibles ainsi que de n’importe quelle taille.

Les images compressées devront être au format WebP ou AVIF (à moins que vous ne réussissiez à nous surprendre avec des formats plus 
légers !)

L’image compressée doit rester la plus lisible et la plus compréhensible possible (donc pas d’images de 1px par 1px). 

Les vidéos d’entrées pourront être dans tous les formats possibles ainsi que de n’importe quelle taille.

Pour les vidéos compressées libre à vous de trouver le meilleur format, codec ou taille pour obtenir le meilleur rapport
qualité/poids !

La ressource compressée ne doit pas dépassée le poids maximal désiré.

Les technologies, langages, bibliothèques ou tout ce que vous réussirez à utiliser devront être open-source à minima et 
si possible maintenus. Cependant, vous n’avez pas le droit de faire appel à d’autres API tierces payantes.


## Faits

La conversion de tout type d'image au format AVIF avec un paramètre pour spécifier le niveau de compression

Les technologies, langages, bibliothèques utilisés sont open-source.

Aucune  API tierces payantes.

Possibilité d'importer une image locale

Un MAGNIFIQUEEEE site web !!!

Pas d’images de 1px par 1px

## Comment tester ??

Executer le Dockerfile du backend et lancer le conteneur docker

Executer le Dockerfile du frontend et lancer le conteneur docker

Tester directement sur le frontend 

localhost:{le port sur lequel le conteneur frontend est écouté}


### Documentation de API

localhost:{le port sur lequel le conteneur backend est écouté}/Numanis/docs



# Pour tester sans docker, cloner le projet et executer les commandes ci-dessous

Dans ce cas, la doc des api est disponible au http://127.0.0.1:8000/Numanis/docs




## Project Setup

```sh
pip install -r requirements.txt
```

### Compile and Hot-Reload for Development


```bash
# Effacez le contenu du dossier media
rm -r media/*
```
### Compile and Hot-Reload for Development

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
