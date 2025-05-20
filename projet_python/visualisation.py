
# Analyse univariée des variables du dataframe data


# Dans votre fichier visualisation.py (ou un nouveau script d'exploration)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



# --- Fonctions d'automatisation ---

def plot_univariate_distributions(df, numeric_cols, categorical_cols, figsize=(8, 4)):
    """
    Génère des histogrammes pour les colonnes numériques et des diagramme à barre
    pour les colonnes catégorielles.

    in:
        df : Le DataFrame à visualiser.
        numeric_cols : Liste des noms de colonnes numériques.
        categorical_cols : Liste des noms de colonnes catégorielles.
        figsize : Taille de base pour chaque figure.
    out: 
    figure
    """
    
 
    print("\n--- Visualisation des Distributions Univariées ---")

    # Distributions pour les colonnes numériques
    print("Tracé des histogrammes pour les colonnes numériques...")
    for col in numeric_cols:
        plt.figure(figsize=figsize)
        sns.histplot(data=df, x=col, kde=True) # kde=True ajoute la courbe de densité
        plt.title(f'Distribution de {col}')
        plt.xlabel(col)
        plt.ylabel('Fréquence')
        plt.tight_layout()
        plt.show()

    # Distributions pour les colonnes catégorielles
    print("Tracé des countplots pour les colonnes catégorielles...")
    for col in categorical_cols:
        plt.figure(figsize=figsize)
        if df[col].nunique() > 10:
             sns.countplot(data=df, y=col, order=df[col].value_counts().index) 
             plt.title(f'Distribution de {col}')
             plt.xlabel('Nombre de véhicules')
             plt.ylabel(col)
        else:
             sns.countplot(data=df, x=col, order=df[col].value_counts().index) 
             plt.title(f'Distribution de {col}')
             plt.xlabel(col)
             plt.ylabel('Nombre de véhicules')
        plt.tight_layout()
        plt.show()



