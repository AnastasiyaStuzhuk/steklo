from django.db import models
from django.forms import ModelForm, Textarea
from datetime import date


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return self.name
# Create your models here.


class Mail(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    widgets = {
        'message': Textarea(attrs={'cols': 80, 'rows': 20}),

    }
    def __str__(self):
        return self.name





