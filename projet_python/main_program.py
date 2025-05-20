# Ceci est notre programme principale où sont appelés toutes nos fonctions

import pretraitement as pret


# PRETRAITEMENT DES DONNEES
chemin_fichier = "imports-85.data"

data = pret.charger_et_nettoyer_auto_data(chemin_fichier)
print(data.head(10))

dataframe_nettoye = charger_et_nettoyer_auto_data(chemin_fichier)

print("DataFrame après nettoyage:")
print(dataframe_nettoye.head())


# VISUALISATION

numeric_features = data.select_dtypes(include=np.number).columns.tolist()
categorical_features = data.select_dtypes(include='object').columns.tolist()

if 'symboling' in numeric_features:
    numeric_features.remove('symboling')
    categorical_features.append('symboling')

numeric_features.remove('price') 
target_col = 'price'

numeric_features_for_dist = numeric_features + [target_col]

plot_univariate_distributions(data, numeric_features_for_dist, categorical_features)


# PREDICTION

## Division des données
X_train, X_test, y_train, y_test = division_donnee(auto_nettoye)

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

# Prédiction
pred_RF = RF.predict(X_test_normalise)
pred_RF

metrics.accuracy_score(y_test, pred_RF)

metrics.f1_score(y_test, pred_RF, average='weighted')








