from django.contrib import admin
from .models import VehicleData

@admin.register(VehicleData)
class VehicleDataAdmin(admin.ModelAdmin):
    list_display = (
        'make', 'body_style', 'fuel_type', 
        'drive_wheels', 'predicted_risk', 'prediction_date'
    )
    list_filter = (
        'predicted_risk', 'make', 'fuel_type', 
        'body_style', 'drive_wheels'
    )
    search_fields = ('make', 'body_style')
    list_per_page = 20
    
    fieldsets = (
        ('Vehicle Information', {
            'fields': (
                'make', 'body_style', 'fuel_type',
                'aspiration', 'num_of_doors', 'drive_wheels',
                'engine_location'
            )
        }),
        ('Technical Specifications', {
            'fields': (
                'engine_type', 'num_of_cylinders', 'fuel_system',
                'normalized_losses', 'wheel_base', 'height',
                'bore', 'stroke', 'compression_ratio', 'peak_rpm'
            )
        }),
        ('Results', {
            'fields': ('predicted_risk', 'prediction_date')
        }),
    )
    readonly_fields = ('prediction_date',)