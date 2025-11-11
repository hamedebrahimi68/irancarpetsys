from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages

@require_http_methods(["GET", "POST"])
def login_view(request):
    """صفحه ورود کاربر"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'خوش آمدید {user.first_name or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور نادرست است')
    
    return render(request, 'auth/login.html')

@login_required(login_url='login')
def dashboard_view(request):
    """صفحه داشبورد (فقط برای کاربران لاگین شده)"""
    return render(request, 'dashboard_app/home_dashboard.html')

@login_required(login_url='login')
def logout_view(request):
    """خروج کاربر"""
    logout(request)
    messages.success(request, 'شما با موفقیت خارج شدید')
    return redirect('login')
