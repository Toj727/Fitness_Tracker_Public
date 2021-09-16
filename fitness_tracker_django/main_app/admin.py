from django.contrib import admin
from .models import Profile, Sleep, WeighIn
from .models import WeighIn

# Register your models here.
admin.site.register(Profile)
admin.site.register(WeighIn)
admin.site.register(Sleep)