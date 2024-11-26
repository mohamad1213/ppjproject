from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('tentang/', views.tentang, name='tentang'),
    path('layanan/', views.layanan, name='layanan'),
    path('produk/', views.produk, name='produk'),
    path('galeri/', views.galeri, name='galeri'),
    path('kontak/', views.kontak, name='kontak'),
]
