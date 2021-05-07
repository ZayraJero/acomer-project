from django.db import models
from django.contrib.auth.models import User



# Create your models fonda here. 

class Restaurant(models.Model):
    """Restaurant info"""
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f"{self.name}"
    #relations
    user =models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True,related_name="restaurants")







class Order(models.Model):
    STATUS_TYPES = (
        ("recibido", "Recibido"),
        ("preparando", "En Preparacion"),
        ("enviando", "En Camino"),
        ("entregado", "Entregado"),
    )
    status = models.CharField(max_length=50, choices=STATUS_TYPES,default="recibido",null=True)
   
    #Relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders",null=True)
    client = models.ForeignKey(to ='user.Client',on_delete=models.CASCADE,related_name="orders",null=True)

    def __str__(self) -> str:
        return f"{self.status}"


class Plate(models.Model):
    STATUS_TYPES = (
        ("primer_tiempo", "Primer Tiempo "),
        ("segundo_tiempo", "Segundo Tiempo"),
        ("tercer_tiempo", "Tercer Tiempo"),
        ("cuarto_tiempo", "Cuarto Tiempo"),
        ("bebidas", "Bebidas"),
        ("Complementos", "Complementos"),
        ("ingredientes_extras", "Ingredientes Extras"),
        ("tacos", "Tacos"),
        ("snack", "Snack"),
    )
    type = models.CharField(max_length=100, choices =STATUS_TYPES, default="primer tiempo")
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    image = models.ImageField(upload_to = "plate_images")

    def __str__(self) -> str:
        return f"{self.type},{self.name}"
    #Relations
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="plates",null=True)


class RestaurantAddress(models.Model):
    """Info de la direccion del restaurante"""
    status = models.BooleanField(default=False)
    street = models.CharField(max_length=75)
    suburb = models.CharField(max_length=100)
    municipality = models.CharField (max_length=50)
    int_number = models.CharField(max_length=10)
    ext_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    link_google =models.CharField(max_length=100)

    #Relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="addresses", null=True)

    def __str__(self) -> str:
        return f"{self.status},{self.street},{self.ext_number},{self.suburb}"

class Menu(models.Model):
    """ menu """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    groupMenu = models.BooleanField(default=True)
    price = models.FloatField(max_length=10)
    image = models.ImageField(upload_to = "menu_images")

    #Relations
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus",null=True) 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="menus",null=True)
    
    def __str__(self) -> str:
        return f"{self.groupMenu},{self.price}"

class MenuPlate(models.Model):
    #Relations
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE,related_name="plates",null=True)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,related_name="plates",null=True)
    #order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="menuses",null=True)

