from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
import stripe
from store.forms import DeliveryForm

from store.models import Cart, Order, Product,Price, SubCategory
from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.core.mail import send_mail


stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
def index(request):
    all_products=Product.objects.all()

    # subCategories=all_products.distinct().values_list('subCategory', flat=True)

    categories = [category for category in Product.Category.choices]

    paginator = Paginator(all_products, 20) # Show 25 contacts per page
    page = request.GET.get('page')
    products = paginator.get_page(page)


    return render(request,'store\index.html',{'products':products,'categories':categories})


def productPerCategory(request,category):
    categories = [category for category in Product.Category.choices]
    if category=="all" :
        # return redirect('index')
        products=Product.objects.all()
    else :
        products=Product.objects.filter(category=category)

    sub_categories = SubCategory.objects.filter(product__in=products).distinct().order_by('name')

    return render(request,'store\productPerCategory.html',{'products':products,'categories':categories, 'subCategories':sub_categories})


def show(request,id):
    product=Product.objects.get(id=id)
    return render(request,'store\show.html',{'product':product})


def addToCard(request,id):
    product=Product.objects.get(id=id)
    order,created=Order.objects.get_or_create(user=request.user, product=product)
    cart,_=Cart.objects.get_or_create(user=request.user)
    if created :
        cart.orders.add(order)
        cart.save()
    else :
        order.quantity +=1
        order.save()

    return redirect('show',id=product.id)


def deleteToCart(request,id):
    cart=get_object_or_404(Cart, user=request.user)
    order=get_object_or_404(Order, id=id)
    cart.orders.remove(order)
    order.delete()
    cart.save()
    return redirect('cart')


def updateQuantity(request):

    order=get_object_or_404(Order, id=request.GET.get('order_id'))
    order.quantity=request.GET.get('value')
    order.save()
    # return HttpResponse(order.id)
    return redirect('cart')



def cart(request):
    cart,_=Cart.objects.get_or_create(user=request.user)
    return render(request,'store\cart.html',context={'orders':cart.orders.all()})




def deliveryAddress(request):

    shopper = request.user  # ou quelque chose de similaire pour récupérer l'objet Shopper lié à l'utilisateur connecté
    initial_data = {
        'full_name': shopper.username,
        'email': shopper.email,
        'phone_number': shopper.phone_number,
    }


    if request.method=="POST":
        form=DeliveryForm(request.POST)

        if form.is_valid():
            return redirect('create-checkout-session')        
    else :
        form=DeliveryForm(initial=initial_data)


    return render(request, 'store/shipping.html',context={'form':form})





def CreateCheckoutSessionView(request):
    
    # if request.method=='POST':

    cart=get_object_or_404(Cart,user=request.user)
    orders=cart.orders.all()


    domain = "https://yourdomain.com"
    if settings.DEBUG:
        domain = "http://127.0.0.1:8000"

    productsInfo=[]
    for order in orders:
        #pour un article(order)
        price = Price.objects.get(product=order.product)



        productsInfo.append(
            {
                'price': price.stripe_price_id,
                'quantity': order.quantity,
            },  
        )

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=productsInfo,
            mode='payment',
            success_url=domain + '/cart/payement/success/',
            cancel_url=domain + '/cart/payement/cancel/',
        )
    return redirect(checkout_session.url)
    # return HttpResponse('GET')



def SuccessView(request):
    return render(request,'store\success.html')


def ConcelView(request):
    return render(request,'store\success.html')


stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
   # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session["customer_details"]["email"]
        line_items = stripe.checkout.Session.list_line_items(session["id"])
        print(session)


        # stripe_price_id = line_items["data"][0]["price"]["id"]
        # price = Price.objects.get(stripe_price_id=stripe_price_id)
        # product = price.product

        # send_mail(
        #     subject="Here is your product",
        #     message=f"Thanks for your purchase. The URL is",
        #         recipient_list=["leranslerans3@gmail.com"],
        #         from_email="abdoulnassertheking@gmail.com"
        #     )
        
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['leranslerans3@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )

    return HttpResponse(status=200)






