from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    dimension = models.CharField(max_length=30)
    colours = models.CharField(max_length=100)
    material = models.CharField(max_length=30)
    image = models.TextField()

    def __str__(self):
        return self.name

# class User(models.model):
#     uid = models.TextField()
