from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponse
from django.shortcuts import render
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . forms import ProductForm
from django.contrib import messages
from . models import Product
from account.models import Profile 
from django.utils.text import slugify


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category, available=True).order_by('-created')
    return render(request,'shop/product/list.html',{'category': category,'categories': categories,'products': products})

def product_detail(request, id, slug):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        product = get_object_or_404(Product,id=id,slug=slug,available=True)
        categories = Category.objects.all()
        return render(request,'shop/product/detail.html',{'product': product, 'categories': categories, 'profile': profile})
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    categories = Category.objects.all()
    return render(request,'shop/product/detail.html',{'product': product, 'categories': categories})

@login_required
def userproduct(request):
    if request.method == 'POST':
        userproduct_form = ProductForm(files=request.FILES, data=request.POST)
        if userproduct_form.is_valid():
            product = userproduct_form.save(commit=False)
            temp = product.name
            product.slug = slugify(temp)
            product.user = request.user
            product.save()
            messages.success(request, 'Product Uploaded Successfully')
        else:
            messages.error(request, 'Error Uploading Your Product')
    else:
        userproduct_form = ProductForm()
    return render(request,'shop/product/uploadproduct.html',{'userproduct_form': userproduct_form})

