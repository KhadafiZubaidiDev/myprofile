from django.urls import path
from . import views

urlpatterns = [
    path('pelatihan/', views.pelatihan, name='pelatihan'),
]