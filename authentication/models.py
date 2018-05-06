from django.db import models

# Create your models here.
from django.db import models
import bcrypt
from django.contrib.auth.models import User


class NetworkDevice(models.Model):
    name = models.CharField(max_length=200, default='Home Network Device')
    password = models.CharField(max_length=256)

    def verify_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf8'), self.password)

    def __str__(self):
        return self.name


class NetworkType(models.Model):
    network_type = models.CharField(max_length=250)

    def __str__(self):
        return self.network_type


class UserNetworkConfig(models.Model):
    config_name = models.CharField(max_length=256)
    #device=models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    network_type = models.ForeignKey(NetworkType, on_delete=models.CASCADE)

    def __str__(self):
        return self.config_name
