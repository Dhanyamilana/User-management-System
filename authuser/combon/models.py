from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Emp(models.Model):  
    empid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
   
    class Meta:  
        db_table = "emp"


class Dhan(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=15)
    dob = models.CharField(max_length=20)
    address = models.CharField(max_length = 100, blank=True)
    # username = models.CharField(max_length=50)
    # password = models.TextField(max_length=50)
    class Meta:
        db_table = "dhan"

@receiver(post_save,sender=User)
def create_dhan(sender,instance,created,**kwargs):
    if created:
        Dhan.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_dhan(sender,instance,**kwargs):
    instance.dhan.save()
