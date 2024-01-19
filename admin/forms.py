# admin/forms.py

from django import forms
from .models import productModel  # Assuming you have a Product model defined in models.py

class ProductForm(forms.ModelForm):
    class Meta:
        model = productModel
        fields = ['P_name', 'P_desc', 'P_category_id', 'P_curstock', 'P_price', 'P_rating']
