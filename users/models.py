from django.db import models
from car.models import CarModel
from django.contrib.auth.models import User

# Create your models here.
# model for comment
class Comment(models.Model):
    # related ar value diye ai field ta access kora jabe
    car = models.ForeignKey(CarModel, on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    
    email = models.EmailField()
    body = models.TextField()
    # auto coment ar date time show korbe
    created_on = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"comment by {self.name}"
    
class orderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

        
    def __str__(self):
        return self.user.username
    
class ItemModel(models.Model):
    order = models.ForeignKey(orderModel, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.car.title