from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f'Name: {self.name} Cost: {self.price}'
    
class Part(models.Model):
    part = models.CharField(max_length=64)
    name = models.ForeignKey(
        Name,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'({self.part}) {self.name}'
    
class Category(models.Model):
    category = models.CharField(max_length=64)
    part = models.ForeignKey(
        Part,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.category}'



class Inventory(models.Model):
    category = models.CharField(max_length=64)
    name = models.CharField(max_length=100)
    part = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.FloatField()
    
class Log(models.Model):
    category = models.CharField(max_length=64)
    name = models.CharField(max_length=100)
    part = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.FloatField()


    
