"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib.auth.views import LogoutView

from django.contrib import admin
from django.urls import path
from store.views import ConcelView, CreateCheckoutSessionView, SuccessView, addToCard, cart, deleteToCart, deliveryAddress, index, productPerCategory, show, stripe_webhook, updateQuantity
from accounts.views import  get_cities, subscribe,signIn_signOut
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('store/<str:category>',productPerCategory,name="productPerCategory"),
    path('product/<int:id>/',show,name="show"),
    path('product/<int:id>/addToCart/',addToCard,name="addToCart"),
    path('product/<int:id>/deleteToCart/',deleteToCart,name="deleteToCart"),
    path('order/updateQuantity/',updateQuantity,name="updateQuantity"),
    # path('order/removeOrder/',removeOrder,name="removeOrder"),
    path('signUp/', subscribe ,name='subscribe'),
    path('login/', signIn_signOut, name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('cart/', cart, name="cart"),
    path('cart/deliveryAddress/', deliveryAddress, name="deliveryAddress"),


    path('cart/create-checkout-session/', CreateCheckoutSessionView, name='create-checkout-session'),
    path('cart/payement/cancel/', ConcelView, name='cancel'),
    path('cart/payement/success/', SuccessView, name='success'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('country/get_cities/', get_cities, name='get_cities'),

]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)