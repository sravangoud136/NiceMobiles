from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.
class Job(models.Model):
    REGISTERED = "REGISTERED"
    IN_PROGRESS="IN_PROGRESS"
    CLOSED = "CLOSED"
    DELIVERED="DELIVERED"
    choices=[
        (REGISTERED, 'Registered'),
        (IN_PROGRESS, 'In Progress'),
        (CLOSED, 'Closed'),
        (DELIVERED, 'Delivered')
    ]
    # id = models.BigIntegerField(primary_key = True)
    warranty_choices=[('In Warranty','In Warranty') , ('Out Warranty','Out warranty'), ('Return Warranty','Return warranty'), ('No Warranty','No warranty'),]
    part_replacement_warranty_choices=[('In Warranty','In Warranty') , ('Out Warranty','Out warranty'),]
    
    device_condition_choices=[('Physical Damage','Physical Damage'),('Water Damage','Water Damage'),('Good Condition','Good Condition'),]
    device_choices=[('Mobile','Mobile'),('Tablet','Tablet')]
    
    jobTitle = models.CharField(max_length=256)
    #jobReferenceNumber=models.CharField(max_length=100, blank=True)
    jobDescription=models.CharField(max_length=500)
    CreatedTime=models.DateTimeField(auto_now_add=True)
    UpdatedTime=models.DateTimeField(auto_now=True)
    jobStatus=models.CharField(max_length=20,choices=choices, default=REGISTERED)
    customerName=models.CharField(max_length=256,null=True)
    customerAddress=models.CharField(max_length=500,null=True)
    customerMobileNumber=models.CharField(max_length=10,null=True)
    EstimatedCompletionDate=models.DateField(default=None,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    device_type = models.CharField(max_length=20,choices=device_choices, default='Mobile')   
    brand = models.CharField(max_length=100,blank=True,null=True)
    model_name= models.CharField(max_length=100,blank=True,null=True)
    imei_num1=models.CharField(max_length=15,blank=True,null=True)
    imei_num2=models.CharField(max_length=15,blank=True,null=True)
    part_code=models.CharField(max_length=25,blank=True,null=True)
    part_replacement_warranty=models.CharField(max_length=20,choices=part_replacement_warranty_choices, default='Out Warranty')
    #inwarranty select -- no of days description
    purchased_from=models.CharField(max_length=100,blank=True,null=True)
    warranty_status=models.CharField(max_length=20,choices=warranty_choices, default='No Warranty')
    condition_of_set=models.CharField(max_length=20,choices=device_condition_choices, default='Good Condition')
    accessories_sbumitted=models.CharField(max_length=500,blank=True,null=True)
    EstimatedCost=models.FloatField(null=True, blank=True)
    barcode=models.ImageField(upload_to="media",blank=True,null=True)
    
    
    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'91{self.customerMobileNumber}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.customerMobileNumber}_{self.customerName}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)
    
    
    
    def  __str__(self):
        return self.jobTitle+" - "+self.jobStatus
    
    
class ServiceProvider(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    contact_num=models.CharField(max_length=14)
    authorized_service_center_name=models.CharField(max_length=200)
    email_id=models.EmailField(null=True,blank=True)
    Address=models.TextField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    logo=models.ImageField()
    def __str__(self):
        return str(self.user.username)
    
@receiver(post_save, sender=User)
def create_serviceprovider_profile(sender, instance, created, **kwargs):
    if created:
        ServiceProvider.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_serviceprovider_profile(sender, instance, **kwargs):
    instance.serviceprovider.save()   
    
class History(models.Model):
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    updated_time=models.DateTimeField(auto_now=True)
    comment=models.CharField(max_length=400,null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.comment)
    
    
   

        
  

'''class ASC(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    contact_num=models.CharField(max_length=14)
    def __str__(self):
        return str(self.name)

class Handset(models.Model):
    model_name= models.CharField(max_length=100,blank=True,null=True)
    imei_num1=models.CharField(max_length=15,blank=True,null=True)
    imei_num2=models.CharField(max_length=15,blank=True,null=True)
    pop_date=models.DateField(blank=True,null=True)
    purchased_from=models.CharField(max_length=100,blank=True,null=True)
    warranty_status=models.CharField(max_length=100,blank=True,null=True)
    condition_of_set=models.CharField(max_length=100,blank=True,null=True)
    accessories_sbumitted=models.CharField(max_length=500,blank=True,null=True)
    '''
    
    
    
    
        
        

    
