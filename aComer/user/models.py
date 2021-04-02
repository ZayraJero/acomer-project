from django.db import models
from aComer.fonda import models as fmodels

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    email = models.EmailField(unique=True)

class ClientAddress(models.Model):
    alias = models.CharField(max_length=50)
    street = models.CharField(max_length=75)
    suburb = models.CharField(max_length=100)
    municipality = models.CharField (max_length=50)
    state = models.CharField(max_length=50)
    int_number = models.IntegerField(max_length=10)
    ext_number = models.IntegerField(max_length=10)
    #Relations
    client = models.ForeignKey(Client,on_delete=models.PROTECT,related_name="clients")

class Ratings(models.Model):
    RATING_TYPES = (
        ("pesimo","Pesimo"),
        ("malo","Malo"),
        ("regular","Regular"),
        ("bueno","Bueno"),
        ("muy bueno","Muy Bueno"),
    )

    rating = models.CharField(max_length=50,choices=RATING_TYPES,default="muy bueno")

    #Relations
    restaurant = models.ForeignKey(fmodels.Restaurant, on_delete=models.PROTECT, related_name="restaurant_addresses")
    client = models.ForeignKey(Client,on_delete=models.PROTECT,related_name="clients")