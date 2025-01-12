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

# Trie des entrées moyennes par fauteuil de 2022 
region_stats_sorted = region_stats.sort_values(by='entrees_par_fauteuil_2022', ascending=False)

# Affiche les 3 meilleures régions
print("\n3 Top 3 Meilleures régions (entrées moyennes par fauteuil) :")
print(region_stats_sorted.head(3))

# Affiche les 3 pires régions
print("\n3 Top 3 Pires régions (entrées moyennes par fauteuil) :")
print(region_stats_sorted.tail(3))