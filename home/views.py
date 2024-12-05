from django.shortcuts import render, redirect
from kontak.models import Contact
from .forms import ContactForm

def index(request):
    return render (request, 'home.html')

def tentang(request):
    return render (request, 'tentang.html')

def layanan(request):
    return render (request, 'layanan.html')

def produk(request):
    return render (request, 'produk.html')

def galeri(request):
    return render (request, 'galeri.html')

def kontak(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kontak') 
    else:
        form = ContactForm()
    return render(request, 'kontak.html', {'form': form})