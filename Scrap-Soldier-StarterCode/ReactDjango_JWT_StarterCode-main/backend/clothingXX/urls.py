from django.urls import path, include
from clothingXX import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_ClothingXXs),
    path('all/', views.get_all_ClothingXXs),
]
