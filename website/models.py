from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category

class Subcategory(models.Model):
    subcategory = models.CharField(max_length=64)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.subcategory
       
class Part(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name

class Inventory(models.Model):
    category = models.CharField(max_length=64)
    name = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.FloatField()
    
class Log(models.Model):
    category = models.CharField(max_length=64)
    name = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.FloatField()
    time = models.DateField()


    
