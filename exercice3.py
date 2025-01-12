import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

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

# Création du nuage de points avec régression linéaire pour écrans vs entrées
plt.figure(figsize=(10, 6))
sns.regplot(x='ecrans', y='entrees 2022', data=df_2022, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.title('Relation entre le nombre d\'écrans et les entrées annuelles (2022)')
plt.xlabel('Nombre d\'écrans')
plt.ylabel('Entrées annuelles')
plt.grid()
plt.tight_layout()
plt.show()

# Création du nuage de points avec régression linéaire pour fauteuils vs entrées
plt.figure(figsize=(10, 6))
sns.regplot(x='fauteuils', y='entrees 2022', data=df_2022, scatter_kws={'color': 'green'}, line_kws={'color': 'red'})
plt.title('Relation entre le nombre de fauteuils et les entrées annuelles (2022)')
plt.xlabel('Nombre de fauteuils')
plt.ylabel('Entrées annuelles')
plt.grid()
plt.tight_layout()
plt.show()

# La réponse à la question de l'exercice 3 est disponible dans le fichier README
