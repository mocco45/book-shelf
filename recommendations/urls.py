from django.urls import path
from . import views

urlpatterns = [
    path('recommendation', views.index)
]
