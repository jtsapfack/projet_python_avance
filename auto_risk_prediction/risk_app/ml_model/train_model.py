import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
#from pretraitement import *

# Données d'exemple (à remplacer par vos données réelles)
# data = {
    # 'year': [2010, 2015, 2018, 2012, 2019, 2016, 2014, 2017],
    # 'mileage': [120000, 80000, 40000, 95000, 30000, 60000, 110000, 50000],
    # 'engine_size': [1.6, 2.0, 1.4, 1.8, 2.5, 1.6, 2.0, 1.4],
    # 'safety_features': [5, 7, 8, 6, 9, 7, 6, 8],
    # 'accident_history': [2, 0, 0, 1, 0, 1, 3, 0],
    # 'maintenance_records': [3, 5, 7, 4, 8, 6, 2, 7],
    # 'risk_level': [2, 0, 0, 1, 0, 1, 2, 0]
# }

# df = pd.DataFrame(data)

# X = df.drop('risk_level', axis=1)
# y = df['risk_level']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Sauvegarder le modèle
# joblib.dump(model, 'model.pkl')

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



def encode_frequency(df, column):
    """
    Cette fonction convertit les variables qualitatives 
    en valeurs numériques en remplacant les modalités par leur
    fréquence d'apparition
    """
    frequency = df[column].value_counts(normalize=True)  # Calculer la fréquence
    df[column] = df[column].map(frequency)  # Mapper les fréquences
    return df


def division_donnee(df):
    """ 
    Cette fonction divise le jeu de données en données d'entrainement
    et données de test
    """
    
    X = df.iloc[:,1:]
    Y = df.iloc[:,:1]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state=42)
    return X_train, X_test, y_train, y_test


def normaliser_colonne(df, colonnes_a_normaliser, methode='minmax'):
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
    
    df_copie = df.copy()
    for colonne in colonnes_a_normaliser:
        if colonne not in df_copie.columns:
            print(f"Erreur : La colonne '{colonne}' n'existe pas dans le DataFrame.")
            continue
        
        df_copie[colonne] = pd.to_numeric(df_copie[colonne], errors='coerce')

        if df_copie[colonne].isnull().any():
            print(f"Avertissement : La colonne '{colonne}' contient des valeurs non-numériques ou manquantes après conversion. Veuillez les gérer avant la normalisation.")
            continue
        
        colonne_data = df_copie[colonne].dropna().values.reshape(-1, 1)

        if len(colonne_data) == 0:
            print(f"Avertissement : La colonne '{colonne}' ne contient aucune valeur numérique valide à normaliser.")
            continue

        if methode == 'minmax':
            scaler = MinMaxScaler()
        elif methode == 'standard':
            scaler = StandardScaler()
        else:
            print(f"Erreur : Méthode de normalisation '{methode}' non reconnue. Utilisez 'minmax' ou 'standard'.")
            return df
        
        for colonne in colonnes_a_normaliser:        
            df_copie[[colonne]] = scaler.fit_transform(df_copie[[colonne]])
            
    return df_copie

chemin_fichier = "risk_app/ml_model/imports-85.data"

auto_nettoye = charger_et_nettoyer_auto_data(chemin_fichier)

X_train, X_test, y_train, y_test = division_donnee(auto_nettoye)
    
# Application de la normalisation
X_train_normalise = normaliser_colonne(X_train, X_train.select_dtypes(include=np.number).columns, methode='minmax')
X_test_normalise = normaliser_colonne(X_test, X_train.select_dtypes(include=np.number).columns, methode='minmax')

# Application de l'encodage par fréquence sur les variables qualitatives
Xtr = X_train_normalise.select_dtypes(include='object').columns.tolist()
Xte = X_test_normalise.select_dtypes(include='object').columns.tolist()
for column in Xtr :
    X_train_normalise = encode_frequency(X_train_normalise, column)
    
for column in Xte :
    X_test_normalise = encode_frequency(X_test_normalise, column)
    
 
 # Création du modèle
model  = RandomForestClassifier(random_state=42)

# Apprentissage du modèle
model .fit(X_train_normalise,y_train)

# Prédiction
# pred_RF = RF.predict(X_test_normalise)
# pred_RF

# Sauvegarder le modèle
joblib.dump(model, 'risk_app/ml_model/model.pkl')