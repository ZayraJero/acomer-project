from user.models import Client
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from fonda.models import Restaurant
from user.models import Client



# Register your models here.
class RestaurantInline(admin.StackedInline):
    model = Restaurant
    can_delete = False
    verbose_name_plural = 'restaurants'

class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'clients'

class UserAdmin(BaseUserAdmin):
    inlines = (RestaurantInline,ClientInline)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Restaurant)
admin.site.register(Client)