from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, ManyToManyField, ImageField, OneToOneField
from django.db.models.fields import DecimalField, DateField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal

# Create your models here.

class Profile(Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    image = CharField(
        max_length=500, default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinclipart.com%2Fpindetail%2FiiRmhwb_png-file-svg-default-profile-picture-free-clipart%2F&psig=AOvVaw0UIbCGa2c2jIE9q58q0tbE&ust=1631224577068000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJi5hKGv8PICFQAAAAAdAAAAABAD')
    starting_weight = DecimalField(max_digits=5, decimal_places=2, min_value=Decimal('80.00'))
    weight_goal = DecimalField(max_digits=5, decimal_places=2, min_value=Decimal('91.00'))

    def __str__(self):
        return self.user.username


class WeighIn(Model):
    date = DateField(default=date.today())
    weight = DecimalField(max_digits=5, decimal_places=2, min_value=Decimal('80.00'))

    def __str__(self):
        return self.weight
        
class Sleep(Model):
    date = DateField(default=date.today())
    hours = DecimalField(max_digits=3, decimal_places=2, min_value=Decimal('0.50'))

    def __str__(self):
        return self.hours
