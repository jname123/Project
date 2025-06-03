from products.models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# 회원가입 view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

# 로그인 view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# 로그아웃 view
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

def mypage_view(request):
    my_products = Product.objects.filter(seller=request.user)
    return render(request, 'users/mypage.html', {'my_products': my_products})