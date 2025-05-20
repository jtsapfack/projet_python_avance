from django.shortcuts import render, redirect
from .forms import VehicleRiskForm
from .models import VehicleData
import joblib
import os
from django.conf import settings
import pandas as pd

def load_model():
    model_path = os.path.join(settings.BASE_DIR, 'risk_app', 'ml_model', 'model.pkl')
    return joblib.load(model_path)

def home(request):
    return render(request, 'risk_app/home.html')
 
def encode_frequency(df, column):
    """
    Cette fonction convertit les variables qualitatives 
    en valeurs numériques en remplacant les modalités par leur
    fréquence d'apparition
    """
    frequency = df[column].value_counts(normalize=True)  # Calculer la fréquence
    df[column] = df[column].map(frequency)  # Mapper les fréquences
    return df

def predict_risk(request):
    if request.method == 'POST':
        form = VehicleRiskForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            
            # Load ML model
            model = load_model()
            
            # Prepare data for prediction (adapt to your model's requirements)
            input_data = [
                [
                    vehicle.normalized_losses,
                    vehicle.make,
                    vehicle.fuel_type,
                    vehicle.aspiration,
                    vehicle.num_of_doors,
                    vehicle.body_style,
                    vehicle.drive_wheels,
                    vehicle.engine_location,
                    vehicle.wheel_base,
                    vehicle.height,
                    vehicle.engine_type,
                    vehicle.num_of_cylinders,
                    vehicle.fuel_system,
                    vehicle.bore,
                    vehicle.stroke,
                    vehicle.compression_ratio,
                    vehicle.peak_rpm
                ]
            ]
            
            # Make prediction (adapt to your model)
            risk_level = model.predict(input_data)[0]
            risk_mapping = {0: 'Faible', 1: 'Moyen', 2: 'Élevé'}
            vehicle.predicted_risk = risk_mapping.get(risk_level, 'Inconnu')
            vehicle.save()
            
            return redirect('results', pk=vehicle.pk)
    else:
        form = VehicleRiskForm()
    
    return render(request, 'risk_app/prediction.html', {'form': form})

def results(request, pk):
    vehicle = VehicleData.objects.get(pk=pk)
    return render(request, 'risk_app/results.html', {'vehicle': vehicle})