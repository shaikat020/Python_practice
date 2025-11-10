from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactInfo
from .forms import Contactform


# Create your views here.
def home(request):
    contacts = ContactInfo.objects.all()
    return render(request, 'contact/home.html', {'contacts' : contacts})

def add_contact(request):
    form = Contactform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'contact/forms.html',{'form':form, 'title' : 'Add Contact'})

def edit_contact(request, id):
    contact = get_object_or_404(ContactInfo, id=id)
    form = Contactform(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return('home')
    return render(request, 'contact/forms.html',{'form':form, 'title':'Edit Contact'})

def delete_contact(request,id):
    contact = get_object_or_404(ContactInfo, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request,'contact/delete.html', {'contact':contact})