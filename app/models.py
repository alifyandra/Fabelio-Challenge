from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    dimension = models.CharField(max_length=30)
    colours = models.CharField(max_length=100)
    material = models.CharField(max_length=30)
    image = models.TextField()
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    seen = ArrayField(models.IntegerField(), default=list, blank=True)
    
    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)