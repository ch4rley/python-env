from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, UserUploadEditForm
from . models import Profile 
from django.contrib import messages
from shop.models import Product
from django.utils.text import slugify

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
    
@login_required
def dashboard(request):
    user = request.user
    products = Product.objects.filter(user=request.user).order_by('-created')
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'products': products, 'user': user})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, 'Error Updating Your Profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form': user_form, 'profile_form': profile_form, 'profile': profile})


@login_required
def UserUploadEdit(request, id):
    product = get_object_or_404(Product,id=id,user=request.user)
    products = Product.objects.filter(user=request.user, available=True).order_by('-created')
    if request.method == 'POST':
        form = UserUploadEditForm(instance=product, data=request.POST, files=request.FILES)
        if form.is_valid():
            productt = form.save(commit = False)
            product.slug = slugify(productt.name)
            product.price = productt.price
            product.photo = productt.photo
            product.name = productt.name
            product.available = productt.available
            product.description = productt.description
            product.category = productt.category
            product.stock = productt.stock
            product.save()
            messages.success(request, 'Profile Updated Successfully')
            return render(request,'account/dashboard.html',{'products': products})
        else:
            messages.error(request, 'Error Updating Your Profile')
    else:
        form = UserUploadEditForm(instance=product)
    return render(request,'account/editupload.html',{'form': form, 'product': product})


@login_required
def UserUploadDelete(request, id):
    product = get_object_or_404(Product,id=id,user=request.user,available=True)
    if request.user == product.user:
        product.delete()
        return HttpResponse("Delete Successful")
    return HttpResponse("Success")
