from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField(max_length=250)
    email= models.EmailField()
    phonenumber = models.CharField(max_length=120)
    address = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name