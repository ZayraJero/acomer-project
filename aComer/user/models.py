from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CustomerAddress(models.Model):
    alias = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    neighborhood = models.CharField(max_length=50)
    delegation = models.CharField(max_length=50)
    int_num = models.CharField(max_length=5)
    ext_num = models.CharField(max_length=5)
    zip_code = models.CharField(max_length=5)

def __str__(self):
        return f"{self.alias}"

class OrderFood(models.Model):

    STATUS_TYPES = (
        ("recibido", "Recibido"),
        ("preparando", "En preparación"),
        ("enviado", "En camino"),
        ("entregado", "Entregado"),
    )
    status = models.CharField(max_length=50, choices=STATUS_TYPES, default="recibido")

    #Relations
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name="items")
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name="menus")
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="customers")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name="restaurants")

class Rating(models.Model):
    
    RATING_TYPES = (
        ("muy mala", "Muy mala"),
        ("mala", "Mala"),
        ("buena", "Buena"),
        ("muy buena", "Muy buena"),
        ("perfecta", "Perfecta"),
    )
    rating = models.CharField(max_length=50, choices=STATUS_TYPES, default="recibido")

    #Relations
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="customers")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name="restaurants")
    
class Restaurant(models.Model):
    rest_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

def __str__(self):
        return f"{self.rest_name} {self.phone}"

class Menu(models.Model):
    starter = models.CharField(max_length=100)
    first_course = starter = models.CharField(max_length=100)
    main_dish = starter = models.CharField(max_length=100)
    dessert = starter = models.CharField(max_length=100)
    drink = starter = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default="5")

    #Relations
    order_food = models.ForeignKey(OrderFood, on_delete=models.PROTECT, related_name="orders")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name="restaurants")
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name="items")

class Item(models.Model):
    item_food = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    #Relations
    order_food = models.ForeignKey(OrderFood, on_delete=models.PROTECT, related_name="orders")
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name="menus")






