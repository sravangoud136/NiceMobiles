from django.forms import fields
from home import models
from django import forms
class JobForm(forms.ModelForm):
    class Meta:
        model=models.Job
        exclude=['jobReferenceNumber']
        widgets ={
            'jobTitle':forms.TextInput(attrs={'class':'form-control'}),
            'jobDescription':forms.Textarea(attrs={'class':'form-control'}),
            'jobStatus':forms.Select(attrs={'class':'form-control'}),
            'customerName':forms.TextInput(attrs={'class':'form-control'}),
            'customerAddress':forms.Textarea(attrs={'class':'form-control'}),
            'customerMobileNumber':forms.TextInput(attrs={'class':'form-control'}),
            'EstimatedCompletionDate':forms.DateInput(attrs={'class':'form-control'}),
            
            
        }
        