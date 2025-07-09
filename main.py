import pandas as pd

# Charger le fichier CSV d'origine
input_csv = 'data/series_longues_passages_urgences_2017_2023.csv'  # à adapter si besoin
output_csv = 'data/moyenne_passages_par_dep.csv'

df = pd.read_csv(input_csv, sep=';', engine='python')

# Calculer la moyenne journalière des passages par département et libellé
# On groupe par 'dep' et 'libelle_dep' pour garder l'information du nom du département
grouped = df.groupby(['dep', 'libelle_dep'])['nb_passages'].mean().reset_index()
grouped.rename(columns={'nb_passages': 'moyenne_journaliere_passages'}, inplace=True)

grouped.to_csv(output_csv, index=False)
print(grouped)
