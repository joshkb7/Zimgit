from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default='0.0')
    description = models.TextField(max_length=1000, help_text='Enter a brief description of this item.')
    image = models.TextField(max_length=300, default='', blank=True)
    file = models.FileField(blank=True, upload_to='users/static/users/downloads/')
    paypal_button = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name