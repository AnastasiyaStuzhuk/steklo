from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Mail)
admin.site.register(Product)


from django.contrib import admin
from landing import views