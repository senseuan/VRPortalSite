from django.shortcuts import render, redirect
from .forms import VRReviewForm

def index(request):
    if request.method == 'POST':
        form = VRReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # после отправки остаёмся на той же странице
    else:
        form = VRReviewForm()
    return render(request, 'vr_site/index.html', {'form': form})

def gallery(request):
    return render(request, 'vr_site/gallery.html')

def experiences(request):
    return render(request, 'vr_site/experiences.html')