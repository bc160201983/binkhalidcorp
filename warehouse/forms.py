from django import forms
from .models import Category, Stock

class RawCategoryForm(forms.Form):
    name = forms.CharField()


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = [
            'name',
            'categories',
            'length',
            'weight',
            'remarks',
        ]




