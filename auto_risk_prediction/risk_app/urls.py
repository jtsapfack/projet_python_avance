from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_risk, name='predict_risk'),
    path('results/<int:pk>/', views.results, name='results'),
]