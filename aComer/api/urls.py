from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import (
    #Restaurant
    ListRestaurantsAPIView,
    CreateRestaurantAPIView,
    RetrieveRestaurantAPIView,
    UpdateRestaurantAPIView,
    DeleteRestaurantAPIView,
    RetrieveRestaurantAddressAPIView,
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
    RetrieveRestaurantAddressesAPIView,
    UpdateRestaurantAddressesAPIView,
    DeleteRestaurantAddressesAPIView,
    #Menu
    ListMenusAPIView,
    CreateMenusAPIView,
    RetrieveMenusAPIView,
    UpdateMenusAPIView,
    DeleteMenusAPIView,
    #client
    ListClientsAPIView,
    CreateClientsAPIView,
    RetrieveClientsAPIView,
    UpdateClientsAPIView,
    DeleteClientsAPIView,
    #client addresses
    ListAddressesAPIView,
    CreateAddressesAPIView,
    RetrieveAddressesAPIView,
    UpdateAddressesAPIView,
    DeleteAddressesAPIView,
    #raitings
    ListRatingsAPIView,
    CreateRatingsAPIView,
    RetrieveRatingsAPIView,
    UpdateRatingsAPIView,
    DeleteRatingsAPIView,
    )

urlpatterns=[
    #Restaurant
    path("restaurant/",ListRestaurantsAPIView.as_view(),name="list-restaurants"),
    path("restaurant/create/",CreateRestaurantAPIView.as_view(),name="create-restaurants"),
    path("restaurant/<int:pk>/detail/",RetrieveRestaurantAPIView.as_view(),name="detail-restaurants"),
    path("restaurant/<int:pk>/update/",UpdateRestaurantAPIView.as_view(),name="update-restaurants"),
    path("restaurant/<int:pk>/delete/",DeleteRestaurantAPIView.as_view(),name="delete-restaurants"),
    path("restaurant/<int:pk>/address/",RetrieveRestaurantAddressAPIView.as_view(),name="detail-restaurantsOrder"),
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
    path("raddress/create/",CreateRestaurantAddressesAPIView.as_view(),name="create-raddress"),
    path("raddress/<int:pk>/detail/",RetrieveRestaurantAddressesAPIView.as_view(),name="detail-raddress"),
    path("raddress/<int:pk>/update/",UpdateRestaurantAddressesAPIView.as_view(),name="update-raddress"),
    path("raddress/<int:pk>/delete/",DeleteRestaurantAddressesAPIView.as_view(),name="delete-raddress"),
    #Menu
    path("menu/",ListMenusAPIView.as_view(),name="list-menu"),
    path("menu/create/",CreateMenusAPIView.as_view(),name="create-menu"),
    path("menu/<int:pk>/detail/",RetrieveMenusAPIView.as_view(),name="detail-menu"),
    path("menu/<int:pk>/update/",UpdateMenusAPIView.as_view(),name="update-menu"),
    path("menu/<int:pk>/delete/",DeleteMenusAPIView.as_view(),name="delete-menu"),
    #client
    path("client/",ListClientsAPIView.as_view(),name="list-client"),
    path("client/create/",CreateClientsAPIView.as_view(),name="create-client"),
    path("client/<int:pk>/detail/",RetrieveClientsAPIView.as_view(),name="detail-client"),
    path("client/<int:pk>/update/",UpdateClientsAPIView.as_view(),name="update-client"),
    path("client/<int:pk>/delete/",DeleteClientsAPIView.as_view(),name="delete-client"),
    #client address
    path("address/",ListAddressesAPIView.as_view(),name="list-address"),
    path("address/create/",CreateAddressesAPIView.as_view(),name="create-address"),
    path("address/<int:pk>/detail/",RetrieveAddressesAPIView.as_view(),name="detail-address"),
    path("address/<int:pk>/update/",UpdateAddressesAPIView.as_view(),name="update-address"),
    path("address/<int:pk>/delete/",DeleteAddressesAPIView.as_view(),name="delete-address"),
    #ratings
    path("rating/",ListRatingsAPIView.as_view(),name="list-rating"),
    path("rating/create/",CreateRatingsAPIView.as_view(),name="create-rating"),
    path("rating/<int:pk>/detail/",RetrieveRatingsAPIView.as_view(),name="detail-rating"),
    path("rating/<int:pk>/update/",UpdateRatingsAPIView.as_view(),name="update-rating"),
    path("rating/<int:pk>/delete/",DeleteRatingsAPIView.as_view(),name="delete-rating"),


]