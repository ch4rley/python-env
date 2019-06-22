from django import forms 
from django.contrib.auth.models import User
from . models import Product #, Image


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length= 20, label='Title')
    class Meta:
        model = Product
        fields = ('name', 'category', 'photo', 'description', 'price', 'stock', 'available' )
        
# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Image') 
#     class Meta:
#         model = Image
#         fields = ('file',)
