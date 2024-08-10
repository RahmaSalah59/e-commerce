from django.shortcuts import redirect, render
from .models import Category, Product,Order,Customer
from django.views.generic import DetailView, ListView, TemplateView
from .forms import signupfrom
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def home(request):
    items = Product.objects.all()
    categorise = Category.objects.all()
    return render(request , 'index.html',{'items':items,'categorise':categorise})


    
class Get_item(DetailView):
    model = Product
    template_name = "review.html"
    context_object_name = "item"
    

def sign_up(request):
    if request.method=='POST':
        form = signupfrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')
    else:
        form = signupfrom()
    return render (request,'signup.html',{'form':form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        print(f"Form is valid: {form.is_valid()}")
        if form.is_valid():
                print("SDCSCC")
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)    
                    return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request) 
    return redirect ('/')

class about(TemplateView):
    template_name = 'about.html'

def category(request,slug):
    specified_category = Category.objects.get(slug=slug)
    related_products = Product.objects.filter(category=specified_category)
    return render(request, 'categorise.html',{'related_products':related_products,'specified_category':specified_category})