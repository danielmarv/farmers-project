from django import forms
from .models import *

class products_form(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'origin', 'category', 'packaging', 'harvest_date', 'cost_price', 'Shelf_life',]
        widgets = {
            'harvest_date':
            forms.DateInput(format='%d-%m-%Y'),
        }
        input_formats = ['%d-%m-%Y']

class Sell_poultry_form(forms.ModelForm):
    class Meta:
        model = Sell_poultry
        fields = ['product', 'caption', 'price', 'picture',]

class Sell_cattle_form(forms.ModelForm):
    class Meta:
        model = Sell_cattle
        fields = ['product', 'caption', 'price', 'picture',]

class Sell_legumes_form(forms.ModelForm):
    class Meta:
        model = Sell_legumes
        fields = ['product', 'caption', 'price', 'picture',]

class Sell_roottubers_form(forms.ModelForm):
    class Meta:
        model = Sell_roottubers
        fields = ['product', 'caption', 'price', 'picture',]

class Sell_cereals_form(forms.ModelForm):
    class Meta:
        model = Sell_cereals
        fields = ['product', 'caption', 'price', 'picture',]