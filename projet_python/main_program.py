# Ceci est notre programme principale où sont appelés toutes nos fonctions

import pretraitement as pret
import visualisation as vis



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

# SAUVEGARDE

sauvegarde("Figures", data_nettoye)

# PREDICTION

## Model entrainé
RF = train_model(data_nettoye)

pred_RF = RF.predict(X_test_normalise)
pred_RF

metrics.accuracy_score(y_test, pred_RF)

metrics.f1_score(y_test, pred_RF, average='weighted')





