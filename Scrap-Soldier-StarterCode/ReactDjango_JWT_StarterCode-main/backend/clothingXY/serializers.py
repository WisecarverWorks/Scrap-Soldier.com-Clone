from rest_framework import serializers
from .models import ClothingXY

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class ClothingXYSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingXY
        fields = ['id', 'size', 'price', 'product_number', 'product_name', 'quantity', 'image', 'user_id']
        depth = 1
