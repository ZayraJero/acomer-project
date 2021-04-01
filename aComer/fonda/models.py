from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models fonda here.

class Restaurant(models.Model):
    """Restaurant info"""
    rest_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f"{self.rest_name}"

class Order(models.Model):
    STATUS_TYPES = (
        ("recibido, Recibido"),
        ("preparando, En Preparacion"),
        ("enviando, En Camino"),
        ("entregado, Entregado"),
    )
    status = models.CharField(max_length=50, choices=STATUS_TYPES,default="recibido")


class RastaurantAddress(models.Model):
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
    entrance = models.CharField(max_length=150)
    first_time = models,CharField(max_length=150)
    main_course = models.CharField(max_length=150)
    dessert = models.CharField(max_length=150)
    drink = models.CharField(max_length=150)
    cost = models.FloatField()

    #Relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name="restaurant_addresses")
