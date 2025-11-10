from django.db import models

# Create your models here.
class contactinfo(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.CharField(max_length=11)
    address=models.CharField(null=True, blank=True)
    
    def __str__(self):
        return self.name