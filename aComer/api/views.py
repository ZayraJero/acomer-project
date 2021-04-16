#from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from fonda.models import (
    Restaurant,
    Plate,
    Order,
    RestaurantAddress,
    Menu,
    MenuPlate,
    )
from user.models import (
    Client,
    ClientAddress,
    Rating,
)
from .serializers import (
    #restaurants
    RestaurantListSerializer,
    RestaurantSerializer,
    RestaurantOrdersSerializer,
    #plates
    PlateListSerializer,
    PlateSerializer,
    #orders
    OrderListSerializer,
    #restaurant addresses
    RestaurantAddressesListSerializer,
    RestaurantAddressesSerializer,
    #menu
    MenusListSerializer,
    MenusSerializer,
    #client
    ClientsListSerializer,
    ClientsSerializer,
    #client addresses
    ClientAddressesListSerializer,
    ClientAddressesSerializer,
    #raitings
    RaitingsListSerializer
    )

#RestaurantViews
class ListRestaurantsAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()#.order_by("created_at")
    serializer_class = RestaurantSerializer 

class CreateRestaurantAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer

class RetrieveRestaurantAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer   

class UpdateRestaurantAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer

class DeleteRestaurantAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer 

class RetrieveRestaurantOrdersAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantOrdersSerializer


#PlateView

class ListPlatesAPIView(generics.ListAPIView):
    queryset = Plate.objects.all()#.order_by("created_at")
    serializer_class = PlateSerializer

class CreatePlatesAPIView(generics.CreateAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateListSerializer

class RetrievePlatesAPIView(generics.RetrieveAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateListSerializer

class UpdatePlatesAPIView(generics.UpdateAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateListSerializer

class DeletePlatesAPIView(generics.DestroyAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer

#Order

class ListOrdersAPIView(generics.ListAPIView):
    queryset = Order.objects.all()#.order_by("created_at")
    serializer_class = OrderListSerializer

class CreateOrdersAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class RetrieveOrdersAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class UpdateOrdersAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class DeleteOrdersAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

#RestaurantAddres

class ListRestaurantAddressesAPIView(generics.ListAPIView):
    queryset = RestaurantAddress.objects.all()#.order_by("created_at")
    serializer_class = RestaurantAddressesSerializer

class CreateRestaurantAddressesAPIView(generics.CreateAPIView):
    queryset = RestaurantAddress.objects.all()
    serializer_class = RestaurantAddressesListSerializer

class RetrieveRestaurantAddressesAPIView(generics.RetrieveAPIView):
    queryset = RestaurantAddress.objects.all()
    serializer_class = RestaurantAddressesListSerializer

class UpdateRestaurantAddressesAPIView(generics.UpdateAPIView):
    queryset = RestaurantAddress.objects.all()
    serializer_class = RestaurantAddressesSerializer

class DeleteRestaurantAddressesAPIView(generics.DestroyAPIView):
    queryset = RestaurantAddress.objects.all()
    serializer_class = RestaurantAddressesSerializer


#Menu
class ListMenusAPIView(generics.ListAPIView):
    queryset = RestaurantAddress.objects.all()#.order_by("created_at")
    serializer_class = MenusSerializer

class CreateMenusAPIView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenusListSerializer

class RetrieveMenusAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenusListSerializer

class UpdateMenusAPIView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenusSerializer

class DeleteMenusAPIView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenusSerializer

#client

class ListClientsAPIView(generics.ListAPIView):
    queryset = Client.objects.all()#.order_by("created_at")
    serializer_class = ClientsSerializer

class CreateClientsAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsListSerializer

class RetrieveClientsAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsListSerializer

class UpdateClientsAPIView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer

class DeleteClientsAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer

#client address

class ListAddressesAPIView(generics.ListAPIView):
    queryset = ClientAddress.objects.all()#.order_by("created_at")
    serializer_class = ClientAddressesSerializer

class CreateAddressesAPIView(generics.CreateAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressesListSerializer

class RetrieveAddressesAPIView(generics.RetrieveAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressesListSerializer

class UpdateAddressesAPIView(generics.UpdateAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressesListSerializer

class DeleteAddressesAPIView(generics.DestroyAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressesSerializer

#ratings

class ListRatingsAPIView(generics.ListAPIView):
    queryset = Rating.objects.all()#.order_by("created_at")
    serializer_class = RaitingsListSerializer

class CreateRatingsAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RaitingsListSerializer

class RetrieveRatingsAPIView(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RaitingsListSerializer

class UpdateRatingsAPIView(generics.UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RaitingsListSerializer

class DeleteRatingsAPIView(generics.DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RaitingsListSerializer