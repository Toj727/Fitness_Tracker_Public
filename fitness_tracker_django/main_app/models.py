import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, ManyToManyField, ImageField, OneToOneField
from django.db.models.deletion import CASCADE
from django.db.models.fields import DecimalField, DateField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal

# Create your models here.

class Profile(Model):
    user = OneToOneField(User, on_delete=models.CASCADE,default= "Null")
    image = CharField(
        max_length=500, default='https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg')
    starting_weight = DecimalField(max_digits=5, decimal_places=2, default="150.00")
    weight_goal = DecimalField(max_digits=5, decimal_places=2, default="150.00")

    def __str__(self):
        return self.user.username

class WeighIn(Model):
    date = DateField(verbose_name=_("Date"))
    weight = DecimalField(max_digits=5, decimal_places=2)
    user = ForeignKey(User, on_delete=CASCADE, related_name='weigh_ins', default=1)
    

    def __str__(self):
        return str(self.weight)

    class Meta:
        ordering = ['date']
        
class Sleep(Model):
    date = DateField(verbose_name=_("Date"))
    hours = DecimalField(max_digits=4, decimal_places=2)
    user = ForeignKey(User, on_delete=CASCADE, related_name="sleeps", default=1)

    def __str__(self):
        return str(self.hours)

    class Meta:
        ordering = ['date']
