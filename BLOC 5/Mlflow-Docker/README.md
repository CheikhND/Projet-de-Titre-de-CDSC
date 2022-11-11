Exécution de tous les composants avec Docker Compose

```
docker-compose -f docker-compose.yml up --build
```


Pour exécuter uniquement le serveur mlflow avec Docker, en faisant suivre le port vers localhost:5000

```
docker-compose -f compose-server.yml up --build
```


### Démarrer un serveur mlflow pour l'interface utilisateur sur le port 5000


```
mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlflow-artifact-root \
--host 0.0.0.0
```

### Entrainement d'un modèle

Le script `clf-train-registry.py` utilise l'ensemble de données sklearn sur le cancer du sein, forme un classificateur simple de forêt aléatoire.

```
python clf-train-registry.py clf-model "http://localhost:5000" --outputTestData test.csv
```

### Entrainement du modèle sur le port 1234


```
export MLFLOW_TRACKING_URI=http://localhost:5000
mlflow models serve -m models:/clf-model/Staging -p 1234 -h 0.0.0.0
```

## Faire des prédictions

Pour les données d'inférence dans un fichier appelé `test.csv`, exécutez ce qui suit :

```
curl http://localhost:1234/invocations  -H 'Content-Type: text/csv' --data-binary @test.csv
```


Cela renvoie aux valeurs de probabilités prédites.

## Cleaning up

Arrêt de tous les conteneurs avec la commande suivante :

```
docker-compose down
```


