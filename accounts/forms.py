from django import forms

from accounts.models import City, Country, Shopper


class SubcribeForm(forms.ModelForm):

   

    class Meta:
        model = Shopper
        fields = ('username', 'first_name', 'email','password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
                'style': ' background-color:red;',
                'placeholder': 'Name'
                }),
            'first_name': forms.TextInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
                'style': ' background-color:red;',
                'placeholder': 'Name'
                }),

            'email': forms.EmailInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
                'style': '',
                'placeholder': 'Email'
                }),
            'password': forms.PasswordInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.",
                'style': '',
                'placeholder': 'Password'
                })

        }
    

        

    
