from django.db import models

# Create your models here.
class Device(models.Model): 
    hostname = models.CharField(max_length=20)
    IPAddress = models.CharField(max_length=20)
    deviceType = models.CharField(max_length=20)
    family = models.CharField(max_length=20)
    model = models.CharField(max_length=20, default = "")

    def __str__(self):
        return self.hostName

#add objects = models.Manager()