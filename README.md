# Bank ETL pipeline 

## presentation
ce projet simule un flux de données bancaire complet.L'objectif est de démontrer ka mise en place de pipeline **ETL (Extract, Transform, Load)** automatisé pour garantir la qualité des données financières avant leur stockage.

##  Architecture du Projet
1. **Extraction** : Génération de 500 transactions via la librairie `Faker`.
2. **Transformation** : Nettoyage avec `Pandas` (gestion des doublons, des valeurs nulles et normalisation).
3. **Chargement** : Injection des données structurées dans une base de données `SQL`.

4. ##  Technologies utilisées
* **Python 3.14**
* **Bibliothèques** : Pandas, Faker, SQLite3

* ##  Comment lancer ce projet
1. Installer les dépendances : `pip install pandas faker`
2. Lancer les scripts dans l'ordre :
   - `python 1generation_donee.py`
   - `python 2transformation.py`
   - `python 3chargement_sql.py`
