import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


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

# Sépare les variables explicatives (X) et la variable cible (y)
X = df_2021[['ecrans', 'fauteuils', 'population_commune']]
y = df_2021['entrees_annuelles']

# Divise les données en ensembles d'entraînement (80%) et de test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

print("Modèle de régression entraîné.")

# Prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Calcul des métriques
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Coefficient de détermination (R²) : {r2:.2f}")
print(f"Erreur moyenne absolue (MAE) : {mae:.2f}")

