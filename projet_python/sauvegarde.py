
import visualisation as vis
import numpy as np


def sauvegarde(save_directory, data_for_plotting) :
    
    numeric_features_plotting = data_for_plotting.select_dtypes(include=np.number).columns.tolist()
    categorical_features_plotting = data_for_plotting.select_dtypes(include='object').columns.tolist()

    target_col = 'symboling' # La colonne cible pour les relations
    # rappelons ici qu'on classer les caractéristiques des voitures selon leurs niveaux de risque

    numeric_features_all = numeric_features_plotting

    # Liste des colonnes numériques pour les nuages de points vs cible (symboling : exclut la cible)
    numeric_features_for_scatter = [col for col in numeric_features_plotting if col != target_col]

    print(f"\nDébut de la génération et sauvegarde des graphiques dans '{save_directory}'... 2pson_B")

    # Analyse univariée
    vis.plot_univariate_distributions(data_for_plotting, numeric_features_all, categorical_features_plotting, save_dir=save_directory)

    vis.plot_numerical_relationships(data_for_plotting, numeric_features_all, target_col=target_col, save_dir=save_directory)
    vis.plot_categorical_numerical_relationships(data_for_plotting, categorical_features_plotting, numerical_col=target_col, save_dir=save_directory, max_categories=10)