from django.conf import settings
from django.db import models

from accounts.models import Shopper

from django.templatetags.static import static


class SubCategory(models.Model):
    name=models.fields.CharField(max_length=200)
    logo=models.ImageField(blank=True,null=True)

    
    def __str__(self) -> str:
        return self.name



# Create your models here.
class Product(models.Model):
    name=models.fields.CharField(max_length=128)
    description=models.fields.TextField(blank=True)
    price=models.fields.FloatField(default=0.0)
    qStock=models.fields.IntegerField(default=0)
    image=models.ImageField(upload_to="products", blank=True,null=True,default='static/images/default.jpg')
    stripe_product_id = models.CharField(max_length=100)
        


    class Category(models.TextChoices):
        VETEMENTS = 'VT'
        COSMETIQUES = 'CM'
        ELECTRONIQUES = 'EC'
    
    category=models.fields.CharField(choices=Category.choices,max_length=5)
    subCategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name




# Order==Article
class Order(models.Model):
    user=models.ForeignKey(Shopper, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.fields.IntegerField(default=1)


    def __str__(self):
        return '{} ({})'.format(self.product.name,self.quantity)
    


# Cart==Panier
class Cart(models.Model):
    user=models.OneToOneField(Shopper, on_delete=models.CASCADE)
    orders=models.ManyToManyField(Order)
    ordered=models.fields.BooleanField(default=False)
    ordered_date=models.DateTimeField(null=True, blank=True, default=None)

    
    def __str__(self):
        return '{} ({})'.format(self.user.username,self.orders.count())
    


#pour le payement en ligne
class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_price_id = models.CharField(max_length=100)
    price_in_stripe = models.IntegerField(default=0)  # cents
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    


