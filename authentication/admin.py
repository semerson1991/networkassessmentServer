from django.contrib import admin

from .models import NetworkType, NetworkDevice, UserNetworkConfig

# Register your models here.

admin.site.register(NetworkType)
admin.site.register(NetworkDevice)
admin.site.register(UserNetworkConfig)