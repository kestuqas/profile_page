from django.urls import path
from . import views


urlpatterns = [
    path('', views.activity, name='activity-page'),
    path('about/', views.about, name='about-page'),
]