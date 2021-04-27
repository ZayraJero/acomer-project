from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import (
    #Restaurant
    ListRestaurantsAPIView,
    RetrieveRestaurantAPIView,
    UpdateRestaurantAPIView,
    DeleteRestaurantAPIView,
    RetrieveRestaurantAddressAPIView,
    RetrieveRestaurantOrdersAPIView,
    RetrieveRestaurantMenusAPIView,

    #Plate
    ListPlatesAPIView,
    CreatePlatesAPIView,
    RetrievePlatesAPIView,
    UpdatePlatesAPIView,
    DeletePlatesAPIView,
    #order
    ListOrdersAPIView,
    CreateOrdersAPIView,
    RetrieveOrdersAPIView,
    UpdateOrdersAPIView,
    DeleteOrdersAPIView,
    #restaurant addreses
    ListRestaurantAddressesAPIView,
    CreateRestaurantAddressesAPIView,
    CreateRestAddressesAPIView,
    RetrieveRestaurantAddressesAPIView,
    RetrieveUpdateRestaurantAddressesAPIView,
    RetrieveDeleteRestaurantAddressesAPIView,
    #Menu
    ListMenusAPIView,
    CreateMenusAPIView,
    RetrieveMenusAPIView,
    UpdateMenusAPIView,
    DeleteMenusAPIView,
    #CreateMenuUnicAPIView,
    #client
    ListClientsAPIView,
    RetrieveClientsAPIView,
    CreateClientAPIView,
    UpdateClientsAPIView,
    DeleteClientsAPIView,
    ClientAddressAPIView,
    ClientOrdersAPIView,
    CreateClientAddressesAPIView,
    #client addresses
    ListAddressesAPIView,
    CreateAddressesAPIView,
    RetrieveAddressesAPIView,
    RetrieveDeleteAddressesAPIView,
    RetrieveUpdateAddressesAPIView,
    #raitings
    ListRatingsAPIView,
    CreateRatingsAPIView,
    RetrieveRatingsAPIView,
    UpdateRatingsAPIView,
    DeleteRatingsAPIView,
    #platillo
    ListMenuPlateAPIView,
    CreateMenuPlateAPIView,
    RetrieveMenuPlateAPIView,
    UpdateMenuPlateAPIView,
    DeleteMenuPlateAPIView,
    )

urlpatterns=[
    #Restaurant
    path("restaurant/",ListRestaurantsAPIView.as_view(),name="list-restaurants"),
    path("restaurant/create/",CreateRestaurantAddressesAPIView.as_view(),name="create-raddress"),
    #path("restaurant/create/",CreateRestaurantAddressesAPIView.as_view(),name="create-restaurants"),
    path("restaurant/<int:pk>/detail/",RetrieveRestaurantAPIView.as_view(),name="detail-restaurants"),
    path("restaurant/<int:pk>/update/",UpdateRestaurantAPIView.as_view(),name="update-restaurants"),
    path("restaurant/<int:pk>/delete/",DeleteRestaurantAPIView.as_view(),name="delete-restaurants"),
    ####
    path("restaurant/<int:pk>/address/",RetrieveRestaurantAddressAPIView.as_view(),name="detail-restaurantsAddress"),
    path("restaurant/<int:pk>/orders/",RetrieveRestaurantOrdersAPIView.as_view(),name="detail-restaurantsOrders"),
    path("restaurant/<int:pk>/menus/",RetrieveRestaurantMenusAPIView.as_view(),name="detail-restaurantsMenus"),

    #plate
    path("plate/",ListPlatesAPIView.as_view(),name="list-plate"),
    path("plate/create/",CreatePlatesAPIView.as_view(),name="create-plate"),
    path("plate/<int:pk>/detail/",RetrievePlatesAPIView.as_view(),name="detail-plate"),
    path("plate/<int:pk>/update/",UpdatePlatesAPIView.as_view(),name="update-plate"),
    path("plate/<int:pk>/delete/",DeletePlatesAPIView.as_view(),name="delete-plate"),
    #order
    path("order/",ListOrdersAPIView.as_view(),name="list-plate"),
    path("order/create/",CreateOrdersAPIView.as_view(),name="create-plate"),
    path("order/<int:pk>/detail/",RetrieveOrdersAPIView.as_view(),name="detail-plate"),
    path("order/<int:pk>/update/",UpdateOrdersAPIView.as_view(),name="update-plate"),
    path("order/<int:pk>/delete/",DeleteOrdersAPIView.as_view(),name="delete-plate"),
    #restaurantaddres
    path("raddress/",ListRestaurantAddressesAPIView.as_view(),name="list-raddress"),
    path("raddress/create/",CreateRestAddressesAPIView.as_view(),name="create-raddress"),
    path("raddress/<int:pk>/detail/",RetrieveRestaurantAddressesAPIView.as_view(),name="detail-raddress"),
    path("raddress/<int:pk>/update/",RetrieveUpdateRestaurantAddressesAPIView.as_view(),name="update-raddress"),
    path("raddress/<int:pk>/delete/",RetrieveDeleteRestaurantAddressesAPIView.as_view(),name="delete-raddress"),
    #Menu
    path("menu/",ListMenusAPIView.as_view(),name="list-menu"),
    path("menu/create/",CreateMenusAPIView.as_view(),name="create-menu"),
    path("menu/<int:pk>/detail/",RetrieveMenusAPIView.as_view(),name="detail-menu"),
    path("menu/<int:pk>/update/",UpdateMenusAPIView.as_view(),name="update-menu"),
    path("menu/<int:pk>/delete/",DeleteMenusAPIView.as_view(),name="delete-menu"),
    #client
    path("client/",ListClientsAPIView.as_view(),name="list-client"),
    path("client/register/",CreateClientAPIView.as_view(),name="create-client"),#crear sin address
    path("client/create/",CreateClientAddressesAPIView.as_view(),name="create-client"),#crear con address
    path("client/<int:pk>/detail/",RetrieveClientsAPIView.as_view(),name="detail-client"),
    path("client/<int:pk>/update/",UpdateClientsAPIView.as_view(),name="update-client"),
    path("client/<int:pk>/delete/",DeleteClientsAPIView.as_view(),name="delete-client"),
    path("client/<int:pk>/address/",ClientAddressAPIView.as_view(),name="retrieve-client-address"),
    path("client/<int:pk>/order/",ClientOrdersAPIView.as_view(),name="retrieve-client-order"),
    #client address
    path("address/",ListAddressesAPIView.as_view(),name="list-address"),
    path("address/create/",CreateAddressesAPIView.as_view(),name="create-address"),
    path("address/<int:pk>/detail/",RetrieveAddressesAPIView.as_view(),name="detail-address"),
    #path("address/<int:pk>/delete/",DeleteAddressesAPIView.as_view(),name="delete-address"),
    path("address/<int:pk>/delete/",RetrieveDeleteAddressesAPIView.as_view(),name="delete-address"),
    path("address/<int:pk>/update/",RetrieveUpdateAddressesAPIView.as_view(),name="detail-update-address"),##funciona pero se puede mejorar

    #ratings
    #path("rating/",ListRatingsAPIView.as_view(),name="list-rating"),
    path("rating/create/",CreateRatingsAPIView.as_view(),name="create-rating"),
    path("rating/<int:pk>/detail/",RetrieveRatingsAPIView.as_view(),name="detail-rating"),
    #path("rating/<int:pk>/update/",UpdateRatingsAPIView.as_view(),name="update-rating"),
    #path("rating/<int:pk>/delete/",DeleteRatingsAPIView.as_view(),name="delete-rating"),
    #menu-plate
    path("platillo/",ListMenuPlateAPIView.as_view(),name="list-platillo"),
    path("platillo/create/",CreateMenuPlateAPIView.as_view(),name="create-platillo"),
    path("platillo/<int:pk>/detail/",RetrieveMenuPlateAPIView.as_view(),name="detail-platillo"),
    path("platillo/<int:pk>/update/",UpdateMenuPlateAPIView.as_view(),name="update-platillo"),
    path("platillo/<int:pk>/delete/",DeleteMenuPlateAPIView.as_view(),name="delete-platillo"),

]