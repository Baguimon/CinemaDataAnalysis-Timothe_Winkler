import pandas as pd

# Charge les données
file_path = "data/cinemas.csv"
df = pd.read_csv(file_path)

# Filtre pour garder uniquement l'année 2022
df_2022 = df[df['entrees 2022'].notna()]
