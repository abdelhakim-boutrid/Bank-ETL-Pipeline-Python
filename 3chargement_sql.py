import pandas as pd
import sqlite3

# 1. On charge nos données
df = pd.read_csv("transactions_propres.csv")

# 2. Connexion
connexion = sqlite3.connect("ma_banque.db")
curseur = connexion.cursor()

# 3. Création de la table (On s'assure que id_transaction et id_client sont TEXT)
curseur.execute("DROP TABLE IF EXISTS transactions") # On nettoie l'ancienne table qui a buggé
requete_creation_table = """
CREATE TABLE transactions (
    id_transaction TEXT,
    id_client TEXT,
    date_transaction TEXT,
    montant REAL,
    devise TEXT,
    statut TEXT
)
"""
curseur.execute(requete_creation_table)

# 4. LE CORRECTIF : On force Pandas à envoyer les IDs en format String (texte)
# On convertit les colonnes problématiques en string avant l'envoi
df['id_transaction'] = df['id_transaction'].astype(str)
df['id_client'] = df['id_client'].astype(str)

# Maintenant on injecte
df.to_sql("transactions", connexion, if_exists="append", index=False)

# 5. On valide et on ferme
connexion.commit()
connexion.close()

print("Cette fois c'est la bonne ! Les données sont dans la base SQL.")