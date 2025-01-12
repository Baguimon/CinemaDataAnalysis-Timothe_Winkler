import pandas as pd

# Charge les données
file_path = "data/cinemas.csv"
df = pd.read_csv(file_path)

# Filtre pour l'année 2021
df_2021 = df[df['entrees 2021'].notna()]
df_2021 = df_2021[['ecrans', 'fauteuils', 'population de la commune', 'entrees 2021']]

# Renommer pour plus de clarté
df_2021.columns = ['ecrans', 'fauteuils', 'population_commune', 'entrees_annuelles']

print("Aperçu des données pour 2021 :")
print(df_2021.head())
