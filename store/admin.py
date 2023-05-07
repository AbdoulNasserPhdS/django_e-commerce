from django.contrib import admin
from store.models import Price, SubCategory
from store.models import Cart, Order, Product

# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','price','category')


admin.site.register(Product,CategoryAdmin)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Price)
admin.site.register(SubCategory)