import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Charger les données
file_path = "data/cinemas.csv"
df = pd.read_csv(file_path)

# Sélection des colonnes nécessaires
df_2021 = df[['ecrans', 'fauteuils', 'population de la commune', 'entrees 2021']].dropna()
df_2021.columns = ['ecrans', 'fauteuils', 'population_commune', 'entrees_annuelles']

# Variables explicatives (X) et cible (y)
X = df_2021[['ecrans', 'fauteuils', 'population_commune']]
y = df_2021['entrees_annuelles']

# Divise en ensemble d'entraînement et de test (80% / 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# **Étape 2 : Entraîner un modèle de régression linéaire**
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModèle de régression entraîné.")

# **Étape 3 : Évaluer les performances du modèle**
# Faire des prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Calcul des métriques
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"\nCoefficient de détermination (R²) sur 2021 : {r2:.2f}")
print(f"Erreur moyenne absolue (MAE) sur 2021 : {mae:.2f}")

# **Étape 4 : Tester le modèle sur les données de 2022**
# Prépare les données pour 2022
df_2022 = df[['ecrans', 'fauteuils', 'population de la commune', 'entrees 2022']].dropna()
df_2022.columns = ['ecrans', 'fauteuils', 'population_commune', 'entrees_annuelles']

# Variable explicatives (X) et cible (y) pour 2022
X_2022 = df_2022[['ecrans', 'fauteuils', 'population_commune']]
y_2022 = df_2022['entrees_annuelles']

# Faire des prédictions sur les données de 2022
y_2022_pred = model.predict(X_2022)

# Ajout des prédictions au DataFrame
df_2022['predicted_entrees'] = y_2022_pred

# Compare les prédictions avec les valeurs réelles
print("\nComparaison des prédictions avec les valeurs réelles pour 2022 (échantillon) :")
print(df_2022[['entrees_annuelles', 'predicted_entrees']].head())

# Calcul des métriques pour 2022
r2_2022 = r2_score(y_2022, y_2022_pred)
mae_2022 = mean_absolute_error(y_2022, y_2022_pred)

print(f"\nCoefficient de détermination (R²) sur 2022 : {r2_2022:.2f}")
print(f"Erreur moyenne absolue (MAE) sur 2022 : {mae_2022:.2f}")

# La réponse à la question de l'exercice 4 est disponible dans le fichier README
