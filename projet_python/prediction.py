
import pretraitement as pret
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

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
    
    
def supprimer_variables_correlees(df, seuil=0.8):
    """
    Supprime les colonnes avec une forte corrélation linéaire.

    Paramètres :
    - df : DataFrame pandas avec uniquement les variables numériques.
    - seuil : valeur absolue du coefficient de corrélation au-dessus duquel on supprime une variable.

    Retour :
    - df sans les colonnes trop corrélées.
    - liste des colonnes supprimées.
    """
    # Calcul de la matrice de corrélation
    corr_matrix = df.select_dtypes(include=np.number).corr().abs()

    # Prendre la partie supérieure de la matrice (triangle supérieur)
    upper = corr_matrix.where(
        pd.DataFrame(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool), 
                     columns=corr_matrix.columns, 
                     index=corr_matrix.index)
    )

    # Trouver les colonnes à supprimer
    colonnes_a_supprimer = [col for col in upper.columns if any(upper[col] > seuil)]
    
    # Supprimer ces colonnes du DataFrame
    df_reduit = df.drop(columns=colonnes_a_supprimer)

    return df_reduit
    

def train_model(data) :
    
    data = supprimer_variables_correlees(data, seuil=0.8)
    ## Division des données
    X_train, X_test, y_train, y_test = division_donnee(data)

    ## Application de la normalisation
    X_train_normalise = normaliser_colonne(X_train, X_train.select_dtypes(include=np.number).columns, methode='minmax')
    X_test_normalise = normaliser_colonne(X_test, X_train.select_dtypes(include=np.number).columns, methode='minmax')

    ## Application de l'encodage par fréquence sur les variables qualitatives
    Xtr = X_train_normalise.select_dtypes(include='object').columns.tolist()
    Xte = X_test_normalise.select_dtypes(include='object').columns.tolist()
    for column in Xtr :
    X_train_normalise = encode_frequency(X_train_normalise, column)

    for column in Xte :
    X_test_normalise = encode_frequency(X_test_normalise, column)

    ## Random Forest

    ### Création du modèle
    RF = RandomForestClassifier(random_state=42)

    ### Apprentissage du modèle
    RF.fit(X_train_normalise,y_train)
    
    return RF
    

