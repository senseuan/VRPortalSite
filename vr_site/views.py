from django.shortcuts import render, redirect
from .forms import VRReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = VRReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VRReviewForm()
    return render(request, 'vr_site/index.html', {'form': form})

def gallery(request):
    return render(request, 'vr_site/gallery.html')

def experiences(request):
    return render(request, 'vr_site/experiences.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'vr_site/register.html', {'form': form})