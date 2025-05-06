from django.shortcuts import redirect, render
import json, os
from django.conf import settings
from .models import Message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


def intro(request):
    return render(request, "base/intro.html")

# Load alerts from JSON
def load_alerts_from_file():
    json_path = os.path.join(settings.BASE_DIR, 'data', 'alerts_json.json')
    with open(json_path, 'r') as f:
        return json.load(f)
@login_required
@never_cache

def home(request):
    alerts = load_alerts_from_file()
    context = {'alertings': alerts}
    return render(request, "base/home.html", context)

@login_required
@never_cache
def alerts(request, pk):
    alerts = load_alerts_from_file()
    alert = next((a for a in alerts if str(a['id']) == pk), None)
    
    messages = Message.objects.filter(alert_id=pk).order_by('-timestamp')

    if request.method == "POST":
        username = request.POST.get('username', 'Anonymous')
        content = request.POST.get('content')
        if content:
            Message.objects.create(alert_id=pk, username=username, content=content)
            return redirect(f'/alerts/{pk}/')

    context = {'alert': alert, 'messages': messages}
    return render(request, "base/alerts.html", context)

@login_required
@never_cache
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'base/signup.html', {'form': form})


@never_cache
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # change to your home view name
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'base/login.html', {'form': form})

@login_required
@never_cache
def logout_view(request):
    logout(request)
    return render(request, 'base/logout.html')  # Instead of redirect('login')

