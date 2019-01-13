from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index),
    path('gen1', views.gen1),
    path('gen2', views.gen2),
    path('gen3', views.gen3),
    path('gen4', views.gen4),
    path('gen5', views.gen5),
    path('gen6', views.gen6),
    path('gen7', views.gen7),
    path('try', views.check),
]
