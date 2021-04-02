from django.db import models

# Create your models here.

class Customer(models.Model):
    """ Customer information """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"{self.first_name, self.last_name}"

class CustomerAddrress(models.Model):
    """ Customer address """
    alias = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    exterior_no = models.CharField(max_length=10)
    interior_no = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)

    # Relations
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="customerAdresses")

    def __str__(self) -> str:
        return f"{self.alias}"

class Review (models.Model):
    """ Customer address """
    title = models.CharField(max_length=50)
    review = models.CharField(max_length=500)

    # Relations
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="reviews")
    business = models.ForeignKey(fonda.Business, on_delete=models.PROTECT, related_name="reviews")

    def __str__(self) -> str:
        return f"{self.title}"

