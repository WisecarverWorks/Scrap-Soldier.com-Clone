
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/cars/', include('cars.urls')),
    path('api/clothingXX', include('clothingXX.urls')),
    path('api/clothingXY', include('clothingXY.urls'))
]
