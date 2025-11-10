from django.contrib import admin
from .models import ContactInfo

@admin.register(ContactInfo)

class ContactInfoAdmin(admin.ModelAdmin):
    list_display=('name','email', 'phonenumber', 'address')
    search_fields=('name','email')
    list_filter=('name','email')
    ordering=('name',)
# Register your models here.
