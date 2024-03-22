from django.db import models

#drink model
class Drink(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name}({self.description})"