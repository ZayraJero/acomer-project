from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from rest_framework import authtoken, serializers#9b47253
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
            "id",
            "type",
            "name",
            "price"
            ]


#Pate
class MenuPlateDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPlate
        fields = [
            "plate",
            ]

class MenuOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPlate
        fields = [
            "menu",
            ]


#Menu

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "id",
            "title",
            "description",
            "price",
            ]

class MenusIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Menu
        fields = [
            "id",
            ]
class PlatesIdSerialiser(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Plate
        fields = ["id"]

#Orders
class OrderListSerializer(serializers.ModelSerializer):
    plates = PlatesIdSerialiser(many = True)
    menus = MenusIdSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "restaurant",
            "client",
            "plates",
            "menus",
        ]

    def create(self, validated_data):
        menu_id=self.validated_data.pop("menus")
        validated_data.pop("menus")
        plates_id=self.validated_data.pop("plates")
        validated_data.pop("plates")
        print("aaaaaaaaaaaaaaaaaa",validated_data)
        order = Order.objects.create(**validated_data)
        for new_menu in menu_id:
            id_menu = new_menu["id"]
            print("ssssssssssssssssss",new_menu["id"])
            menus=list(Menu.objects.filter(id=id_menu))
            print("++++++++++++",order)
            menus[0].order= order
            menus[0].save()
            print("********************",menus[0].order)
        new_array = []
        for new_plates in plates_id:
            id_plates = new_plates["id"]
            platillos =Plate.objects.get(id=id_plates)
            new_array.append(platillos)
            # plates.order = order
            # plates.save()
            #print(plates.order)
        order.plates.set(new_array)
        print("°°°°°°°°°°°°°°°",order.plates)
        print("111111111111",new_array)
        order.save()
        return order

#order status update
class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "status",
        ]

#order detail

class MenusDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Menu
        fields = [
            "id",
            "title"
            ]
class PlatesDetailSerialiser(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Plate
        fields = [
            "id",
            "name"
        ]

#Orders
class OrderDetailSerializer(serializers.ModelSerializer):
    plates = PlatesDetailSerialiser(many = True)
    menus = MenusDetailSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "restaurant",
            "client",
            "plates",
            "menus",
        ]       
            
        

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
            "link_google",
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
            "link_google",
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
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=[
            "username",
            "password",
        ]
        extra_kwargs ={
            "password":{
                "write_only":True
            }
        }
    
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user



class RestaurantCreateSerializer(serializers.ModelSerializer):#restaurant create
    addresses = RestaurantAddressesSerializer(many=True)
    user = UserSerializer()
    class Meta:
        model = Restaurant
        fields = [
            "name",
            "email",
            "phone",
            "addresses",
            "user",
        ]
        
    def create(self, validated_data):
        restaurantId = self.validated_data.pop("addresses")
        userDataId= self.validated_data.pop("user")
        userData = User.objects.create(**userDataId)
        validated_data.pop("addresses")
        validated_data.pop("user")
        array_forms = []
        for restaurant_Id in restaurantId:
          form = RestaurantAddress.objects.create(**restaurant_Id)
          array_forms.append(form)
        restaurant = Restaurant.objects.create(**validated_data)
        restaurant.user=userData
        restaurant.save()
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


#Client

class ClientsListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "email",
            "user"
            ]

    def create(self, validated_data):
        userDataId= self.validated_data.pop("user")
        userData = User.objects.create(**userDataId)
        validated_data.pop("user")
        array_forms = []
        restaurant = Client.objects.create(**validated_data)
        restaurant.user=userData
        restaurant.save()
        restaurant.addresses.set(array_forms)
        return restaurant

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
        fields = [
            "plate",
            "menu",
            "order"
        ]



class MenusListSerializer(serializers.ModelSerializer):
    #dishes = serializers.ListField(child=serializers.CharField(), allow_empty=True,)
    plates = MenuPlateDishesSerializer(many=True)
    class Meta:
        model = Menu
        fields = [
            "title",
            "description",
            "groupMenu",
            "price",
            "restaurant",
            "plates"
        ]
    def create(self, validated_data):
        plate_data = self.validated_data.pop("plates")
        validated_data.pop("plates")
        array_forms = []
        for new_plate in plate_data:
          plate = MenuPlate.objects.create(**new_plate)
          array_forms.append(plate)
          print(new_plate)
        menu = Menu.objects.create(**validated_data)
        menu.plates.set(array_forms)
        return menu


class MenusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "title",
            "description",
            "groupMenu",
            "price",
            "image"
            ]

    # def update(self, instance, validated_data):
    #     plate_data = self.validated_data.pop("plates")
    #     plate_viejo = list(MenuPlate.objects.filter(menu_id=instance.id))
    #     for menus in range(len(plate_data)):
    #         menu_nuevo = super().update(plate_viejo[menus], plate_data[menus])
    #     validated_data.pop("plates")
    #     instance = super().update(instance, validated_data)
    #     menu = super(MenusListSerializer, self).update(instance, validated_data)
    #     menu.save()
    #     return menu

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

# class ClientAddressListSerializer(serializers.ModelSerializer):
#     orders =OrderListSerializer(many=True)
#     class Meta:
#         model = Client
#         fields = [
#             "first_name",
#             "last_name",
#             "phone",
#             "email",
#             "orders"
#             ]


class ClientCreateSerializer(serializers.ModelSerializer):#restaurant create
    addresses = ClientAddressesListSerializer(many=True)
    user = UserSerializer()
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "addresses",
            "user",
        ]
        
    # def create(self, validated_data):
    #     restaurantId = self.validated_data.pop("addresses")
    #     userDataId= self.validated_data.pop("user")
    #     userData = User.objects.create(**userDataId)
    #     validated_data.pop("addresses")
    #     validated_data.pop("user")
    #     array_forms = []
    #     for restaurant_Id in restaurantId:
    #       form = RestaurantAddress.objects.create(**restaurant_Id)
    #       array_forms.append(form)
    #     restaurant = Restaurant.objects.create(**validated_data)
    #     restaurant.user=userData
    #     restaurant.save()
    #     restaurant.addresses.set(array_forms)
    #     return restaurant


    def create(self, validated_data):
        clientId = self.validated_data.pop("addresses")
        userDataId= self.validated_data.pop("user")
        userData = User.objects.create(**userDataId)
        validated_data.pop("addresses")
        validated_data.pop("user")
        array_forms = []
        for client_Id in clientId:
          form = ClientAddress.objects.create(**client_Id)
          array_forms.append(form)
        client = Client.objects.create(**validated_data)
        client.user=userData
        client.save()
        client.addresses.set(array_forms)
        return client


    def update(self, instance, validated_data):
        clients_id = self.validated_data.pop("addresses")
        client_viejo = list(ClientAddress.objects.filter(client_id=instance.id))
        for address in range(len(clients_id)):
            address_nuevo = super().update(client_viejo[address], clients_id[address])
        validated_data.pop("addresses")
        instance = super().update(instance, validated_data)
        client = super(ClientCreateSerializer, self).update(instance, validated_data)
        client.save()
        return client

