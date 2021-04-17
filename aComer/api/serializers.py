from django.db import models
from django.db.models import fields
from rest_framework import serializers
from fonda.models import (
    Menu,
    MenuPlate,
    Order,
    Plate,
    Restaurant,
    RestaurantAddress,
    )
from user.models import (
    Client,
    ClientAddress,
    Rating
)
#Restaurants
class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "email",
            "phone",
            ]
        

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            ]




#Plates



class PlateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = [
            "id",
            "type",
            "name",
            "price",
            ]

class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = [
            "type",
            "name",
            ]


#Orders
class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"



#restaurantAddresses
class RestaurantAddressesListSerializer(serializers.ModelSerializer):
    # restaurant = RestaurantListSerializer()
    class Meta:
        model = RestaurantAddress
        fields = "__all__"
    # def create(self, validated_data):
    #     restaurantId = self.validated_data.pop("restaurant")
    #     restaurant = Restaurant.objects.create(**restaurantId)
    #     validated_data.pop("restaurant")
    #     restaurantAddress= RestaurantAddress.objects.create(restaurant = restaurant,**validated_data)
    #     print(validated_data)
    #     return restaurantAddress


        

class RestaurantAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAddress
        fields = [
            "id",
            "street",
            "suburb",
            "municipality",
            "int_number",
            "ext_number",
            ]

#foreign restaurant
class RestaurantAddressSerializer(serializers.ModelSerializer):
    addresses = RestaurantAddressesSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "addresses"
         ]
#Menu

class MenusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "title",
            "description",
            ]

#Client

class ClientsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "email",
            ]

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            ]

#client address

class ClientAddressesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAddress
        fields = "__all__"

class ClientAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAddress
        fields = [
            "alias",
            "suburb",
            "municipality",
            "int_number",
            "ext_number",
            ]

#rating

class RaitingsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

#menu plate
class MenuPlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPlate
        fields = "__all__"

