from django.db import models
from accounts.models import Customuser

class Appeal(models.Model):
    STATUS_CHOICES = [
        ('new','New'),
        ('in_progress','In Progress'),
        ('clossed','Clossed')
    ]
    
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=50,blank=True)
    phone_number = models.CharField(max_length=15,blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='new')
    assigned_to = models.ForeignKey(Customuser,on_delete=models.SET_NULL,null=True,blank=True)
    photo = models.FileField(upload_to='photos/',blank=True,null=True)
    comment = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)