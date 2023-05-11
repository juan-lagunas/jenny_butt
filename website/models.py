from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category

       
class Part(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name

class Inventory(models.Model):
    category = models.CharField(max_length=64)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()

    @property
    def total_cost(self):
        total = self.price * self.quantity
        return f'{total:.2f}'

    
class Log(models.Model):
    category = models.CharField(max_length=64)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    time = models.DateField()


    
