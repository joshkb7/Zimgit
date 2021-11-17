from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views import generic
from .models import Product


def home(request):
    return render(request, 'users/home.html')

def details(request):
    return render(request, 'users/details.html')

def creators(request):
    return render(request, 'users/creators.html')

def use_cases(request):
    return render(request, 'users/use_cases.html')

def libraries(request):
  return render(request, 'users/libraries.html')

def contact_us(request):
    return render(request, 'users/contact_us.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

#Libraries
class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    queryset = Product.objects.filter()
    template_name = 'users/libraries.html'
