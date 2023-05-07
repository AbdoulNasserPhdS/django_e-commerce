from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from accounts.forms import SubcribeForm
from django.template.loader import render_to_string


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from accounts.models import City


# Create your views here.


# User=get_user_model()

def subscribe(request):
    if (request.method=='POST'):
        subscribeForm=SubcribeForm(request.POST)
        if subscribeForm.is_valid() :
            user=subscribeForm.save()
            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect('index')
    else:
        subscribeForm=SubcribeForm()
    return render(request, 'accounts\signUp.html', {'form':subscribeForm})






def signIn_signOut(request):
    if request.user.is_authenticated:
        # Si connecté, déconnecter l'utilisateur
        logout(request)
        messages.success(request, 'Vous avez été déconnecté avec succès.')
        return redirect('index')
    else:
        # Si pas connecté, tenter de connecter l'utilisateur
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Vous avez été connecté avec succès.')
                # recuperation de l'url stocker depuis le midlleware
                if request.session.get('next_url') :
                    next_url=request.session.get('next_url')
                else:
                    next_url='index'
                return redirect(next_url)
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe invalide.')
    return render(request, 'accounts\login.html')
    


def get_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    city_choices = [(city.id, city.name) for city in cities]

    print(city_choices)
    return JsonResponse({'cities': city_choices})