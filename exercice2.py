import pandas as pd
import matplotlib.pyplot as plt

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


# Création d'un top 10 des régions
top_10_regions = region_stats_sorted.head(10)

# Création du graphique
plt.figure(figsize=(10, 6))
plt.bar(top_10_regions['region administrative'], top_10_regions['entrees_par_fauteuil_2022'], color='skyblue') 

# Ajout des labels et du titre
plt.xlabel('Régions')
plt.ylabel('Entrées moyennes par fauteuil')
plt.title('Entrées moyennes par fauteuil pour les 10 premières régions en 2022')
plt.xticks(rotation=45, ha='right')  # Pour mieux afficher les labels des régions

# Afficher le graphique
plt.tight_layout()  # Ajustement pour éviter les chevauchements
plt.show()