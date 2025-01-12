import pandas as pd

# Charge les données
file_path = "data/cinemas.csv"
df = pd.read_csv(file_path)

# Nettoie les données
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())  # Identifie les valeurs manquantes

# Supposons qu'il manque des données dans 'fauteuils' et 'ecrans', on remplace par la médiane (La médiane est choisie pour éviter d'être influencé par les valeurs extrêmes.)
df['fauteuils'] = df['fauteuils'].fillna(df['fauteuils'].median())
df['ecrans'] = df['ecrans'].fillna(df['ecrans'].median())

# Exemple de vérification : Vérification des valeurs négatives
negatives = df[df[['fauteuils', 'ecrans', 'entrees 2022', 'entrees 2021']] < 0]
if not negatives.empty:
    print("Des valeurs négatives ont été détectées, les voici :")
    print(negatives)
else:
    print("Aucune valeur négative détectée.")


# Exploration
print("\nAperçu des premières données :")
print(df.head())

print("\nStatistiques descriptives :")
print(df[['fauteuils', 'ecrans', 'entrees 2022', 'entrees 2021']].describe())
