#!/usr/bin/env python
# coding: utf-8

# #### Description des données

# This data set consists of three types of entities: (a) the specification of an auto in terms of various characteristics, (b) its assigned insurance risk rating, (c) its normalized losses in use as compared to other cars. The second rating corresponds to the degree to which the auto is more risky than its price indicates. Cars are initially assigned a risk factor symbol associated with its price. Then, if it is more risky (or less), this symbol is adjusted by moving it up (or down) the scale. Actuarians call this process "symboling". A value of +3 indicates that the auto is risky, -3 that it is probably pretty safe.
#
# The third factor is the relative average loss payment per insured vehicle year. This value is normalized for all autos within a particular size classification (two-door small, station wagons, sports/speciality, etc...), and represents the average loss per car per year.
#
# Note: Several of the attributes in the database could be used as a "class" attribute.

# #### Importation des packages nécessaires


# import sklearn as sk # sklearn is imported but not used in the provided code block
# import matplotlib.pyplot as plt # matplotlib is imported but not used
# import seaborn as sns # seaborn is imported but not used
# import csv # csv is imported but not used

# ### Fonction de prétraitement

def charger_et_nettoyer_auto_data(file_path):
    import numpy as np
    import pandas as pd
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    import numpy as np
    """
    Charge le jeu de données automobiles, remplace les '?' par des valeurs manquantes
    et impute ces valeurs manquantes selon le type de colonne.

    in : 
    file_path : Le chemin d'accès au fichier de données ('imports-85.data').


    out : le DataFrame nettoyé avec les valeurs manquantes imputées.
        
    """
    # Définition des noms de colonnes
    column_names = ["symboling", "normalized-losses", "make", "fuel-type",
                    "aspiration", "num-of-doors", "body-style", "drive-wheels",
                    "engine-location", "wheel-base", "length", "width", "height",
                    "curb-weight", "engine-type", "num-of-cylinders", "engine-size",
                    "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
                    "peak-rpm", "city-mpg", "highway-mpg", "price"]

    auto = pd.read_csv(file_path, names=column_names)

    auto[auto == "?"] = np.nan
    col = auto.columns
    for c in range(len(col)):
        if auto[col[c]].dtype == 'int64' or auto[col[c]].dtype == 'float64': # Utilisation des dtypes exacts pour plus de robustesse
            if auto[col[c]].isnull().sum() != 0:
                auto[col[c]] = pd.to_numeric(auto[col[c]])
                auto[col[c]] = auto[col[c]].fillna(auto[col[c]].median())
        else: 
            if auto[col[c]].isnull().sum() != 0:
                if pd.to_numeric(auto[col[c]], errors='coerce').isnull().all():
                     auto[col[c]] = auto[col[c]].fillna(auto[col[c]].mode()[0])
                else:
                    auto[col[c]] = pd.to_numeric(auto[col[c]])
                    auto[col[c]] = auto[col[c]].fillna(auto[col[c]].median())


    return auto

# ## Exemple d'utilisation de la fonction
# if __name__ == "__main__":
#     chemin_fichier = "imports-85.data"

#     dataframe_nettoye = charger_et_nettoyer_auto_data(chemin_fichier)

#     print("DataFrame après nettoyage:")
#     print(dataframe_nettoye.head())


# print(dataframe_nettoye.describe())





def normaliser_colonne(df, colonne_a_normaliser, methode='minmax'):
    import numpy as np
    import pandas as pd
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    import numpy as np
    """
    Normalise une colonne spécifiée dans un DataFrame.

    in:
        df : Le DataFrame contenant la colonne à normaliser.
        colonne_a_normaliser : Le nom de la colonne à normaliser.
        methode : La méthode de normalisation à utiliser ('minmax' ou 'standard').
                       Par défaut, utilise 'minmax'.

    out:
        pandas.DataFrame: Le DataFrame avec la colonne spécifiée normalisée,
                          ou le DataFrame original si la colonne n'existe pas
                          ou n'est pas numérique.
    """
    
    return df_copie

# if __name__ == "__main__":
#     df_normalise_minmax = normaliser_colonne(dataframe_nettoye.copy(), 'price', methode='minmax')
#     print("\nDataFrame avec 'price' normalisée (Min-Max):")
#     print(df_normalise_minmax.head(50))

   

 

