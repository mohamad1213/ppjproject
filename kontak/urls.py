from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='kontak'),
    path('create/', views.create_contact, name='create'),
    path('list/', views.list_contacts, name='list'),
    path('<int:pk>/update/', views.update_contact, name='update'),
    path('<int:pk>/delete/', views.delete_contact, name='delete'),
]
