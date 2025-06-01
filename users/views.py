import form
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
# 회원가입 view
from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 회원가입 후 로그인 페이지로 이동
    else:
        form = SignUpForm()

    return render(request, 'myapp/signup.html', {'form': form})


{'form': form})

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