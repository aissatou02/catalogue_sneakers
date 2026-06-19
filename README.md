# Catalogue Sneakers

## Description

Catalogue Sneakers est une application web développée en Python avec Flask et MySQL.

Elle permet de gérer un catalogue de sneakers grâce à un système CRUD (Create, Read, Update, Delete).

## Technologies utilisées

* Python
* Flask
* MySQL
* HTML
* CSS

## Fonctionnalités

* Affichage des sneakers
* Recherche d'une sneaker
* Ajout d'une sneaker
* Modification d'une sneaker
* Suppression d'une sneaker
* Gestion des marques
* Gestion des catégories
* Gestion des couleurs
* Gestion des pointures

## Structure de la base de données

La base de données contient 5 tables :

* sneakers
* marques
* categories
* couleurs
* tailles

Les tables sont liées grâce à des clés étrangères afin de respecter la normalisation des données.

## Installation

1. Installer Python
2. Installer les dépendances

```bash
pip install -r requirements.txt
```

3. Créer la base de données MySQL

Importer le fichier :

```sql
database.sql
```

4. Modifier les informations de connexion dans :

```python
app.py
```

5. Lancer l'application

```bash
python app.py
```

## Auteur

Projet réalisé dans le cadre du BTS SIO SLAM.
