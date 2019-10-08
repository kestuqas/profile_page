from django.urls import path
from . import views

urlpatterns = [
    path('', views.trial, name='trial-home'),
    path('about/', views.about, name='trial-about'),
]
