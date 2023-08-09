from django import forms
import datetime


class ProductForms(forms.Form):
    name = forms.CharField(max_length=80)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Something about product'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField(min_value=0)
    add_date = forms.DateField(initial=datetime.date.today)
    image = forms.ImageField()
