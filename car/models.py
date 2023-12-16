from django.db import models
from django.contrib.auth.models import User
from brand.models import BrandModel
# Create your models here.

class CarModel(models.Model):
    image = models.ImageField(upload_to='car/uploads/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=15)
    quantity = models.IntegerField()
    
    users = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
     
     
     
    def __str__(self):
        return self.title