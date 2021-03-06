from django.db import models


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"{self.first_name},{self.last_name}"

class ClientAddress(models.Model):
    alias = models.CharField(max_length=50)
    street = models.CharField(max_length=75)
    suburb = models.CharField(max_length=100)
    municipality = models.CharField (max_length=50)
    int_number = models.IntegerField()
    ext_number = models.IntegerField()
    zip_code = models.IntegerField()
    references = models.CharField(max_length=250)
    #Relations
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="addresses", null=True)

    def __str__(self) -> str:
        return f"{self.alias},{self.street},{self.ext_number},{self.suburb}"

class Rating(models.Model):
    RATING_TYPES = (
        ("pesimo","Pesimo"),
        ("malo","Malo"),
        ("regular","Regular"),
        ("bueno","Bueno"),
        ("muy bueno","Muy Bueno"),
    )

    rating = models.CharField(max_length=50,choices=RATING_TYPES,default="muy bueno")

    #Relations
    restaurant = models.ForeignKey(to='fonda.Restaurant', on_delete=models.PROTECT, related_name="ratings",null=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="ratings",null=True)

    def __str__(self) -> str:
        return f"{self.rating}"