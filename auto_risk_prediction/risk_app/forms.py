from django import forms
from .models import VehicleData

class VehicleRiskForm(forms.ModelForm):
    class Meta:
        model = VehicleData
        fields = '__all__'
        widgets = {
            'normalized_losses': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '65',
                'max': '256',
                'step': '0.1'
            }),
            'wheel_base': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '86.6',
                'max': '120.9',
                'step': '0.1'
            }),
            'height': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '47.8',
                'max': '59.8',
                'step': '0.1'
            }),
            'bore': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '2.54',
                'max': '3.94',
                'step': '0.01'
            }),
            'stroke': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '2.07',
                'max': '4.17',
                'step': '0.01'
            }),
            'compression_ratio': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '7',
                'max': '23',
                'step': '0.1'
            }),
            'peak_rpm': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '4150',
                'max': '6600',
                'step': '50'
            }),
        }
        labels = {
            'normalized_losses': 'Pertes normalisées (65-256)',
            'make': 'Marque',
            'fuel_type': 'Type de carburant (diesel, gas)',
            'aspiration': 'Aspiration (std, turbo)',
            'num_of_doors': 'Nombre de portes (four, two)',
            'body_style': 'Style de carrosserie (hardtop, wagon, sedan, hatchback, convertible)',
            'drive_wheels': 'Roues motrices (4wd, fwd, rwd)',
            'engine_location': 'Position du moteur (front, rear)',
            'wheel_base': 'Empattement (86.6-120.9)',
            'height': 'Hauteur du véhicule (47.8-59.8)',
            'bore': 'Alésage (2.54-3.94)',
            'stroke': 'Course (2.07-4.17)',
            'compression_ratio': 'Taux de compression (7-23)',
            'peak_rpm': 'RPM de pointe (4150-6600)',
            'engine_type': 'Type de moteur (dohc, dohcv, l, ohc, ohcf, ohcv, rotor)',
            'num_of_cylinders': 'Nombre de cylindres (eight, five, four, six, three, twelve, two)',
            'fuel_system': 'Système de carburant (1bbl, 2bbl, 4bbl, idi, mfi, mpfi, spdi, spfi)',
        }