import pandas as pd

# Charge les données
file_path = "data/cinemas.csv"
df = pd.read_csv(file_path)

# Calcul des entrées moyennes par fauteuil pour chaque région en 2022
df['entrees_par_fauteuil_2022'] = df['entrees 2022'] / df['fauteuils']

# Calcul de la moyenne par région
region_stats = df.groupby('region administrative')['entrees_par_fauteuil_2022'].mean().reset_index()

# Affiche les entrées moyennes par fauteuil pour chaque région en 2022
print(region_stats)
