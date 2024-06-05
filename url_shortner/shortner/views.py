from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            return render(request, 'shortner/success.html', {'short_url': url.short_url})
    else:
        form = URLForm()
    return render(request, 'shortner/home.html', {'form': form})

def redirect_to_original(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)
