from django.db import models
import uuid

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
    jobTitle = models.CharField(max_length=256)
    jobReferenceNumber=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    jobDescription=models.CharField(max_length=500)
    CreatedTime=models.DateTimeField(auto_now_add=True)
    jobStatus=models.CharField(max_length=20,choices=choices, default=REGISTERED)
    customerName=models.CharField(max_length=256,null=True)
    customerAddress=models.CharField(max_length=500,null=True)
    customerMobileNumber=models.CharField(max_length=10,null=True)
    EstimatedCompletionDate=models.DateField(default=None,null=True)
    
    
    
    def  __str__(self):
        return self.jobTitle+" - "+self.jobStatus
    
class ServiceProvider(models.Model):
    name=models.CharField(max_length=200)
    logo=models.ImageField()
    description=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return str(self.name)
        
        

    
