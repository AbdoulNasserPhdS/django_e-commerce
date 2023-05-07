from django import forms

from accounts.models import City, Country, Shopper


class DeliveryForm(forms.ModelForm):






    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        empty_label=None,
        label='Choisissez un pays',
        widget=forms.Select(attrs={
            'id': 'id_country',
            'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
            'style': '',
            'placeholder': 'Country'
        }))
    city = forms.ModelChoiceField(queryset=City.objects.all(), label='Choisissez une ville', 
                                widget=forms.Select(attrs={
                    'id': 'id_city',
                    'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
                    'style': ' ',
                    'placeholder': 'City'
                    }))
    




    class Meta:
        model=Shopper
        fields=('full_name','country','city','zip_code','phone_number','email')

        # Définition des champs requis
        widgets = {

            'full_name': forms.TextInput(attrs={            
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
                'style': '',
                'placeholder': 'Name'
                }),

            'zip_code': forms.TextInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
                'style': '',
                'placeholder': 'Name'
                }),
                  
            'phone_number': forms.TextInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
                'style': '',
                'placeholder': 'Name'
                }),
            'email': forms.EmailInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
                'style': '',
                'placeholder': 'Email'
                })

        }

        # labels = {
        #     'email': 'Adresse e-mail',
        # }
        # required = {
        #     'email',
        # }


    
    def __init__(self, *args, **kwargs):
        super(DeliveryForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

