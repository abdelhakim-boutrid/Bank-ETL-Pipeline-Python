import pandas as pd

print("Début du nettoyage des données...")

# chargement du fichier sale
df = pd.read_csv("transactions_brutes.csv")

# on affciche le nombre de ligne au depart
print(f"Nombre de lignes avant nettoyage : {len(df)}")

# --- DEBUT DU NETTOYAGE ---

# transaction sans client on jette ca 
# 'dropna' veut dire "drop les Not a Number (valeurs nulles)"
df = df.dropna(subset=['id_client'])

# montant de la transaction non negatif
# On applique la valeur absolue (.abs()) à toute la colonne 'montant'
df['montant'] = df['montant'].abs()

# Si la devise est vide 
# On remplace les cases vides par "EUR"
df['devise'] = df['devise'].replace("", "EUR")
df['devise'] = df['devise'].fillna("EUR") # Sécurité supplémentaire au cas où Pandas voit un "vrai" vide

# --- FIN DU NETTOYAGE ---

#  on regarde combien de lignes il nous reste
print(f"Nombre de lignes après nettoyage : {len(df)}")

# 3. On sauvegarde ce résultat dans un NOUVEAU fichier
df.to_csv("transactions_propres.csv", index=False)

print("Succès ! Tes données sont maintenant propres et sauvegardées dans 'transactions_propres.csv'.")