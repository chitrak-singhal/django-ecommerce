from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartProducts
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products':products})

def test(request):
    products = Product.objects.all()
    return render(request, 'test.html',{'products':products})

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, "Logged in succesfully!")
            return redirect('home')
        else:
            #messages.success(request, "Invalid credentials!")
            return redirect('login')
    else:
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    #messages.success(request,("Logged out successfully!"))
    return redirect('home')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html',{'product':product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_product, created = CartProducts.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_product.quantity += 1
        cart_product.save()

    return redirect('cart_page')

def cart_page(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_products = CartProducts.objects.filter(cart=cart) if cart else []
    return render(request, 'cart.html', {'cart_products': cart_products})