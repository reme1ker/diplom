from django.urls import path
from . import views
from .views import GameDetailView

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
]
