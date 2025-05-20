from django.db import models

class VehicleData(models.Model):
    # Continuous variables
    normalized_losses = models.FloatField(verbose_name="Pertes normalisées (65-256)")
    wheel_base = models.FloatField(verbose_name="Empattement (86.6-120.9)")
    height = models.FloatField(verbose_name="Hauteur (47.8-59.8)")
    bore = models.FloatField(verbose_name="Alésage (2.54-3.94)")
    stroke = models.FloatField(verbose_name="Course (2.07-4.17)")
    compression_ratio = models.FloatField(verbose_name="Taux compression (7-23)")
    peak_rpm = models.FloatField(verbose_name="RPM max (4150-6600)")
    
    # Categorical variables with choices
    MAKE_CHOICES = [
        ('alfa-romero', 'Alfa-Romero'),
        ('audi', 'Audi'),
        ('bmw', 'BMW'),
        ('chevrolet', 'Chevrolet'),
        ('dodge', 'Dodge'),
        ('honda', 'Honda'),
        ('isuzu', 'Isuzu'),
        ('jaguar', 'Jaguar'),
        ('mazda', 'Mazda'),
        ('mercedes-benz', 'Mercedes-Benz'),
        ('mercury', 'Mercury'),
        ('mitsubishi', 'Mitsubishi'),
        ('nissan', 'Nissan'),
        ('peugot', 'Peugot'),
        ('plymouth', 'Plymouth'),
        ('porsche', 'Porsche'),
        ('renault', 'Renault'),
        ('saab', 'Saab'),
        ('subaru', 'Subaru'),
        ('toyota', 'Toyota'),
        ('volkswagen', 'Volkswagen'),
        ('volvo', 'Volvo'),
    ]
    make = models.CharField(max_length=20, choices=MAKE_CHOICES, verbose_name="Marque")
    
    FUEL_TYPE_CHOICES = [
        ('diesel', 'Diesel'),
        ('gas', 'Essence'),
    ]
    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE_CHOICES, verbose_name="Type carburant (diesel, gas)")
    
    ASPIRATION_CHOICES = [
        ('std', 'Standard'),
        ('turbo', 'Turbo'),
    ]
    aspiration = models.CharField(max_length=5, choices=ASPIRATION_CHOICES, verbose_name="Aspiration (std, turbo)")
    
    DOORS_CHOICES = [
        ('four', '4'),
        ('two', '2'),
    ]
    num_of_doors = models.CharField(max_length=4, choices=DOORS_CHOICES, verbose_name="Nombre portes (four, two)")
    
    BODY_STYLE_CHOICES = [
        ('hardtop', 'Hardtop'),
        ('wagon', 'Wagon'),
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchback'),
        ('convertible', 'Convertible'),
    ]
    body_style = models.CharField(max_length=11, choices=BODY_STYLE_CHOICES, verbose_name="Style carrosserie (hardtop, wagon, sedan, hatchback, convertible)")
    
    DRIVE_WHEELS_CHOICES = [
        ('4wd', '4WD'),
        ('fwd', 'FWD'),
        ('rwd', 'RWD'),
    ]
    drive_wheels = models.CharField(max_length=3, choices=DRIVE_WHEELS_CHOICES, verbose_name="Roues motrices (4wd, fwd, rwd)")
    
    ENGINE_LOCATION_CHOICES = [
        ('front', 'Avant'),
        ('rear', 'Arrière'),
    ]
    engine_location = models.CharField(max_length=5, choices=ENGINE_LOCATION_CHOICES, verbose_name="Position moteur (front, rear)")
    
    ENGINE_TYPE_CHOICES = [
        ('dohc', 'DOHC'),
        ('dohcv', 'DOHCV'),
        ('l', 'L'),
        ('ohc', 'OHC'),
        ('ohcf', 'OHCF'),
        ('ohcv', 'OHCV'),
        ('rotor', 'Rotor'),
    ]
    engine_type = models.CharField(max_length=5, choices=ENGINE_TYPE_CHOICES, verbose_name="Type moteur (dohc, dohcv, l, ohc, ohcf, ohcv, rotor)")
    
    CYLINDERS_CHOICES = [
        ('eight', '8'),
        ('five', '5'),
        ('four', '4'),
        ('six', '6'),
        ('three', '3'),
        ('twelve', '12'),
        ('two', '2'),
    ]
    num_of_cylinders = models.CharField(max_length=6, choices=CYLINDERS_CHOICES, verbose_name="Nombre cylindres (eight, five, four, six, three, twelve, two)")
    
    FUEL_SYSTEM_CHOICES = [
        ('1bbl', '1BBL'),
        ('2bbl', '2BBL'),
        ('4bbl', '4BBL'),
        ('idi', 'IDI'),
        ('mfi', 'MFI'),
        ('mpfi', 'MPFI'),
        ('spdi', 'SPDI'),
        ('spfi', 'SPFI'),
    ]
    fuel_system = models.CharField(max_length=4, choices=FUEL_SYSTEM_CHOICES, verbose_name="Système carburant (1bbl, 2bbl, 4bbl, idi, mfi, mpfi, spdi, spfi)")
    
    # Results
    predicted_risk = models.CharField(max_length=50, blank=True)
    prediction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make} - {self.body_style} - Risk: {self.predicted_risk}"