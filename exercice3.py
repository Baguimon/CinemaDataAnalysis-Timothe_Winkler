import pandas as pd

# Charge les données
file_path = "data/cinemas.csv"
df = pd.read_csv(file_path)

# Filtre pour garder uniquement l'année 2022
df_2022 = df[df['entrees 2022'].notna()]

# Calcul des corrélations
correlation_ecrans = df_2022['ecrans'].corr(df_2022['entrees 2022'])
correlation_fauteuils = df_2022['fauteuils'].corr(df_2022['entrees 2022'])

print(f"Corrélation entre le nombre d'écrans et les entrées annuelles (2022) : {correlation_ecrans:.2f}")
print(f"Corrélation entre le nombre de fauteuils et les entrées annuelles (2022) : {correlation_fauteuils:.2f}")
