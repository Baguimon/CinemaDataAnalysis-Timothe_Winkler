# Devoir Python (orienté data) Timothé Winkler

## Récupérer le projet

1. Clonez ce repository sur votre machine en utilisant la commande suivante :

   ```bash
   git clone https://github.com/Baguimon/CinemaDataAnalysis-Timothe_Winkler
   ```
2. Installez les dépendances nécessaires :

Assurez-vous d'avoir Python installé sur votre machine.

Installez les bibliothèques requises (Pandas, Matplotlib, Seaborn, Scikit-learn) en exécutant la commande suivante :

  ```bash
  pip install -r requirements.txt
  ```
Note : Si requirements.txt n'existe pas, vous pouvez installer manuellement les bibliothèques avec :

  ```bash
  pip install pandas matplotlib seaborn scikit-learn
  ```

## Structure du projet

- **data/cinemas.csv**
- **exercice1.py** 
- **exercice2.py**
- **exercice3.py** 
- **exercice4.py**
- **README.md**

### **Commentaires dans le code**
Des commentaires ont été ajoutés dans tout le code afin de faciliter la compréhension de chaque étape. Vous y trouverez des explications sur le traitement des données, les calculs effectués, ainsi que sur les modèles utilisés.

##**Utilisation du projet**

1. Placez-vous dans le répertoire contenant les fichiers Python et les données.

2. Exécutez chaque fichier Python individuellement pour résoudre les exercices correspondants. Par exemple, pour exécuter l'exercice 1, lancez :
   
  ```bash
  python exercice1.py
  ```

## **Réponses aux Questions**
### **Exercice 3 : Corrélations**
Question : Selon vous, quelle est la variable ayant le plus d’impact sur les
entrées annuelles ?
- D'après les analyses de corrélation et les visualisations, le nombre d'écrans semble avoir le plus grand impact sur les entrées annueles. La corrélation entre les écrans et les entrées est plus forte que celle entre les fauteuils et les entrées. De plus, le modèle prédictif montre que le nombre d'écrans est un meilleur prédicteur des entrées, ce qui confirme son influence plus significative.

### **Exercice 4 : Prédictions**
Question : Selon les performances du modèle, le nombre d’écrans ou de
fauteuils est-il un bon prédicteur des entrées ? Expliquez.
- Le nombre d'écrans et de fauteuils semble être un bon prédicteur des entrées annuelles, comme en témoigne le coefficient de détermination (R²) élevé, indiquant que ces variables expliquent bien la variation des entrées. De plus, l'erreur moyenne absolue (MAE) reste relativement faible, ce qui montre que les prédictions du modèle sont précises. Cela suggère que les infrastructures des cinémas, notamment le nombre d'écrans et de fauteuils, jouent un rôle significatif dans le nombre d'entrées.

## Exercice 5: Recommandations stratégiques

### 1. Stratégie proposée :

Sur la base des résultats de l'analyse, **augmenter le nombre d'écrans** serait la stratégie la plus efficace pour augmenter les entrées. En effet, le nombre d'écrans a montré une corrélation plus forte avec les entrées annuelles par rapport aux fauteuils. En ajoutant des écrans, le cinéma peut attirer plus de spectateurs en offrant une plus grande diversité de films et de séances.

### 2. Justification avec des calculs simples :

Prenons les résultats de la corrélation et l'impact de chaque variable sur les entrées annuelles :

- Imaginons qu'un cinéma avec 2 écrans et 120 fauteuils génère un certain nombre d'entrées annuelles. Si l'ajout d'un écran augmente les entrées de X%, cela aurait un impact direct sur le revenu.

Par exemple, si un cinéma avec 2 écrans et 120 fauteuils génère 100 000 entrées annuelles, augmenter de 1 écran pourrait augmenter les entrées de 15% (d'après la corrélation observée dans les analyses).

### Calcul de l'augmentation :

\[
100,000 \times 0.15 = 15,000
\]

Ce qui signifierait une augmentation de 15 000 entrées annuelles. Par contre, si on augmentait les fauteuils (par exemple de 10%), cela aurait un effet plus modéré, étant donné la corrélation plus faible avec les entrées.

### Conclusion :

Ajouter un écran plutôt que des fauteuils serait plus stratégique pour augmenter les entrées, selon les données et les corrélations observées.
