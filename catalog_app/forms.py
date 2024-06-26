from django import forms
from .models import Product_list

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Product_list
        fields = ['name', 'image', 'about_book', 'cloth_type']