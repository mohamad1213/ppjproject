from django.shortcuts import render

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
    return render (request, 'kontak.html')