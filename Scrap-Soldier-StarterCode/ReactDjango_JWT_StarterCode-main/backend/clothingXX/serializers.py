from rest_framework import serializers
from .models import ClothingXX

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class ClothingXXSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingXX
        fields = ['id', 'size', 'price', 'product_number',
                  'product_name', 'quantity', 'image', 'user_id']
        depth = 1
