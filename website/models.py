from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category

class Type(models.Model):
    type = models.CharField(max_length=64)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.type
       
class Part(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name

class Inventory(models.Model):
    category = models.CharField(max_length=64)
    part = models.CharField(max_length=100)
    type = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.FloatField()
    
class Log(models.Model):
    category = models.CharField(max_length=64)
    part = models.CharField(max_length=100)
    type = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.FloatField()
    time = models.DateField()


    
