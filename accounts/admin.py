from django.contrib import admin

from accounts.models import City, Country, Shopper

# Register your models here.


admin.site.register(Shopper)
admin.site.register(City)
admin.site.register(Country)

