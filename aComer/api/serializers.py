from django.db import models
from django.db.models import fields
from django.utils import tree
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
# Restaurants
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
        fields = "__all__"

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


        

class RestaurantAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAddress
        fields = [
            "id",
            "status",
            "street",
            "suburb",
            "municipality",
            "state",
            "int_number",
            "ext_number",
            "zip_code",
            "restaurant"
            ]

#foreign restaurant
class RestaurantAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAddress
        fields = [
            "id",
            "status",
            "street",
            "suburb",
            "municipality",
            "state",
            "int_number",
            "ext_number",
            "zip_code",
            "restaurant"
            ]



# class RestaurantAddressSerializer(serializers.ModelSerializer):
#      restaurant = RestaurantAddressesSerializer()
#      class Meta:
#          model = Restaurant
#          fields = "__all__"

    # def create(self, validated_data):
    #     restaurantId = self.validated_data.pop("restaurant")
    #     restaurant = Restaurant.objects.create(**restaurantId)
    #     validated_data.pop("restaurant")
    #     restaurantAddress= RestaurantAddress.objects.create(restaurant = restaurant,**validated_data)
    #     print(validated_data)
    #     return restaurantAddress




class RestaurantCreateSerializer(serializers.ModelSerializer):#restaurant create
    addresses = RestaurantAddressesSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = [
            "name",
            "email",
            "phone",
            "addresses",
        ]
        
    def create(self, validated_data):
        restaurantId = self.validated_data.pop("addresses")
        validated_data.pop("addresses")
        array_forms = []
        for restaurant_Id in restaurantId:
          form = RestaurantAddress.objects.create(**restaurant_Id)
          array_forms.append(form)
        restaurant = Restaurant.objects.create(**validated_data)
        restaurant.addresses.set(array_forms)
        return restaurant


    def update(self, instance, validated_data):
        adresses_id = self.validated_data.pop("addresses")
        addresses_viejo = list(RestaurantAddress.objects.filter(restaurant_id=instance.id))
        for address in range(len(adresses_id)):
            address_nuevo = super().update(addresses_viejo[address], adresses_id[address])
        validated_data.pop("addresses")
        instance = super().update(instance, validated_data)
        restaurant = super(RestaurantCreateSerializer, self).update(instance, validated_data)
        restaurant.save()
        return restaurant

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
            "id",
            "alias",
            "client"
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



####
class RestaurantOrderSerializer(serializers.ModelSerializer):
    orders = OrderListSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "orders"
         ]


class RestaurantMenuSerializer(serializers.ModelSerializer):
    menus = MenusSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "menus",
         ]


class RestaurantPlatesSerializer(serializers.ModelSerializer):
    plate = MenuPlateSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "plate"
         ]

class RestaurantAddressListSerializer(serializers.ModelSerializer):
    addresses =RestaurantAddressesSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "addresses"
            ]


class RestaurantAddressListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAddress
        fields = [
            "id",
            "status",
            "street",
            "suburb",
            "restaurant",
            ]


class ClientAddressListSerializer(serializers.ModelSerializer):
    addresses =ClientAddressesListSerializer(many=True)
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "addresses"
            ]

class ClientAddressListSerializer(serializers.ModelSerializer):
    orders =OrderListSerializer(many=True)
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "orders"
            ]