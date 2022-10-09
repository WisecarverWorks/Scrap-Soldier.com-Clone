from django.db import models
from authentication.models import User

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class ClothingXX(models.Model):
   # This should have two foreign keys that link to user and the item
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # This will show the object size
    size = models.CharField(max_length=30, null=True, blank=True)
    # Price USD default written as an input mask price on front end later.
    price = models.FloatField(default=0)
    # Product Number written as an input
    product_number = models.IntegerField(null=True, blank=True)
    # Product Name written as an input
    product_name = models.CharField(max_length=30, null=True, blank=True)
    # Quantity of the product as an integer
    quantity = models.IntegerField(null=True, blank=True)
    # Image of the product
    image = models.ImageField(upload_to="clothingXY")

    class Meta:
        db_table = "clothingXX"

    def __str__(self):
        print(self.price, self.quantity, self.size, self.product_name, self.   product_number, self.image, self.user)\
            # returns quantity of product
        return str(self.quantity)
