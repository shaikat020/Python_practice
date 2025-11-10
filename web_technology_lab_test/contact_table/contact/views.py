from django.shortcuts import render, redirect, get_object_or_404
from .models import contactinfo
from .forms import contactinfoform
# Create your views here.
def home(request):
    contact= contactinfo.objects.all()
    return render(request, 'home.html', {'contact' : contact})

def add_contact(request):
    form=contactinfoform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Home')
    return render(request, 'add_contact.html', {'form':form, 'title':'Add Contact'})