from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return '{}/{}'.format(self.name,self.country)



class Shopper(AbstractUser):
    phone_number = models.IntegerField(max_length=20,null=True)
    street_address = models.CharField(max_length=100,null=True, blank=True,default='')
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True, blank=True,default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True, blank=True,default='')
    zip_code = models.IntegerField(max_length=10,null=True)
    full_name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.username