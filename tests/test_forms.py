import datetime

from django.test import TestCase
from django.utils import timezone
from accounts.models import City, Country

from store.forms import DeliveryForm

class DeliveryFormTest(TestCase):
    def test_delivery_form_fullname__field_label(self):
        form = DeliveryForm()
        self.assertTrue(form.fields['full_name'].label == None or form.fields['full_name'].label == 'Full name')

        # Tester si le formulaire d'adresse est valide quand ont soumet

    def test__delivery_form_is_valid(self):


        Country.objects.create(name='Bresil')
        City.objects.create(name='Rio',country=Country.objects.get(id=1))

        form = DeliveryForm(data={
        'full_name': 'heiokh',
        'email': 'A@gmail.com',
        'phone_number': 899888999,
        'zip_code':8999,
        'country': Country.objects.get(id=1),
        'city': City.objects.get(id=1),
    })
        
        self.assertTrue(form.is_valid())
