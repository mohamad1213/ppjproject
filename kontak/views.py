from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'kontak.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

# Create (Menambahkan Pesan)
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:list')  # Redirect ke daftar kontak
    else:
        form = ContactForm()
    return render(request, 'kontak.html', {'form': form})

# Read (Menampilkan Daftar Pesan)
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/list_contacts.html', {'contacts': contacts})

# Update (Memperbarui Pesan)
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact:list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact/update_contact.html', {'form': form})

# Delete (Menghapus Pesan)
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact:list')
    return render(request, 'contact/delete_contact.html', {'contact': contact})
