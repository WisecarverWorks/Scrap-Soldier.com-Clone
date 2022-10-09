from django.urls import path, include
from clothingXY import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_ClothingXYs),
    path('all/', views.get_all_ClothingXYs),
]
