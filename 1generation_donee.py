import pandas as pd
from faker import Faker
import random

# 1. On prépare notre générateur de fausses données (en français)
fake = Faker('fr_FR')

# 2. On crée une liste vide qui va accueillir toutes nos transactions
liste_transactions = []

# 3. On va créer 500 fausses transactions grâce à une boucle
for i in range(500):
    
    # On crée une transaction avec des règles aléatoires
    transaction = {
        "id_transaction": fake.uuid4(), # Génère un identifiant unique complexe
        
        # On simule un bug : 1 fois sur 10, l'ID du client va disparaître (None)
        "id_client": fake.bban() if random.random() > 0.1 else None, 
        
        "date_transaction": fake.date_this_year(), # Une date de cette année
        
        # On génère un montant. Pour simuler une erreur, on autorise des montants négatifs
        "montant": round(random.uniform(-500.0, 5000.0), 2), 
        
        # On choisit une devise au hasard, et parfois on "oublie" de la mettre
        "devise": random.choice(["EUR", "USD", "GBP", "JPY", ""]), 
        
        "statut": random.choice(["Validé", "En attente", "Refusé"])
    }
    
    # On ajoute cette transaction à notre grande liste
    liste_transactions.append(transaction)

# 4. Magie de Pandas : on transforme cette liste en un beau tableau de données
df_transactions = pd.DataFrame(liste_transactions)

# 5. On sauvegarde ce tableau dans un fichier CSV sur ton ordinateur
df_transactions.to_csv("transactions_brutes.csv", index=False)

# Un petit message pour nous dire que tout s'est bien passé
print("Super ! Ton fichier 'transactions_brutes.csv' a ete genere avec succes avec 500 lignes.")