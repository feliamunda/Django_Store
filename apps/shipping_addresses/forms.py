from django.forms import ModelForm
from django import forms


from .models import ShippingAddress

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            'line1','line2','city','state','country','postal_code','reference'
        ]
        labels = {
            'line1' : 'Calle 1',
            'line2' : 'Calle 2',
            'city' : 'Ciudad',
            'state' : 'Estado',
            'country' : 'País',
            'postal_code' : 'Código Postal',
            'reference' : 'Referencias'
        }
        widgets = {
            'line1' : forms.TextInput(attrs={'class':'form-control'}),
            'line2' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'state' : forms.TextInput(attrs={'class':'form-control'}),
            'country' : forms.TextInput(attrs={'class':'form-control'}),
            'postal_code' : forms.TextInput(attrs={ 'class':'form-control',
                                                    'placeholder':'000000'}),
            'reference' : forms.TextInput(attrs={'class':'form-control'})
        }