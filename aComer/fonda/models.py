from django.db import models
from aComer.user import models as umodels

# Create your models fonda here. 

class Restaurant(models.Model):
    """Restaurant info"""
    rest_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f"{self.rest_name}"




class Platillo(models.Model):
    item_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)



class Order(models.Model):
    STATUS_TYPES = (
        ("recibido, Recibido"),
        ("preparando, En Preparacion"),
        ("enviando, En Camino"),
        ("entregado, Entregado"),
    )
    status = models.CharField(max_length=50, choices=STATUS_TYPES,default="recibido")
   
    #Relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name="orders")
    client = models.ForeignKey(umodels.Client,on_delete=models.PROTECT,related_name="orders")




class RestaurantAddress(models.Model):
    """Info de la direccion del restaurante"""
    status = models.BooleanField(default=False)
    street = models.CharField(max_length=75)
    suburb = models.CharField(max_length=100)
    municipality = models.CharField (max_length=50)
    state = models.CharField(max_length=50)
    int_number = models.IntegerField(max_length=10)
    ext_number = models.IntegerField(max_length=10)
    zip_code = models.IntegerField(max_length=5)

    #Relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name="restaurant_addresses")

class Menu(models.Model):
    """ menu """
    menu_type = models.BooleanField(default=True)
    price = models.FloatField(max_length=10)

    #Relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name="menus")

class MenuPlatillo(models.Model):
    #Relations
    platillo = models.ForeignKey(Platillo, on_delete=models.PROTECT,related_name="menus-platillos")
    menu = models.ForeignKey(Menu,on_delete=models.PROTECT,related_name="menus-platillos")
    order = models.ForeignKey(Order,on_delete=models.PROTECT,related_name="menus-platillos")