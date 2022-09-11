from django.forms import fields
from home import models
from django import forms
class JobForm(forms.ModelForm):
    class Meta:
        model=models.Job
        exclude=['author','barcode']
        widgets ={
            'customerName':forms.TextInput(attrs={'class':'form-control'}),
            'customerAddress':forms.Textarea(attrs={'class':'form-control','required':False}),
            'customerMobileNumber':forms.TextInput(attrs={'class':'form-control','placeholder':'Must be 10 Digits Exactly'}),
            'jobTitle':forms.TextInput(attrs={'class':'form-control'}),
            'jobDescription':forms.Textarea(attrs={'class':'form-control','required':False}),
            'jobStatus':forms.Select(attrs={'class':'form-control','onchange':'myFunction(this.value);'}),
            'EstimatedCompletionDate':forms.DateInput(attrs={'class':'form-control','required':False,'placeholder':'DD/MM/YYYY'}),
            'device_type':forms.Select(attrs={'class':'form-control','required':False}),
            'brand':forms.TextInput(attrs={'class':'form-control'}),
            'model_name': forms.TextInput(attrs={'class':'form-control'}),
            'imei_num1':forms.TextInput(attrs={'class':'form-control'}),
            'imei_num2':forms.TextInput(attrs={'class':'form-control'}),
            'part_code':forms.TextInput(attrs={'class':'form-control'}),
            'part_replacement_warranty':forms.Select(attrs={'class':'form-control','required':False}),
            'pop_date':forms.DateInput(attrs={'class':'form-control','required':False}),
            'purchased_from':forms.TextInput(attrs={'class':'form-control','required':False}),
            'warranty_status':forms.Select(attrs={'class':'form-control','required':False}),
            'condition_of_set':forms.Select(attrs={'class':'form-control','required':False}),
            'accessories_sbumitted':forms.TextInput(attrs={'class':'form-control','required':False}),
            'EstimatedCost': forms.TextInput(attrs={'class':'form-control'}),
            
            

            
            
            
            
        }
        
class HistoryForm(forms.ModelForm):
    class Meta:
        model=models.History
        fields="__all__"
        
# class ASCLoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model=models.ServiceProvider
#         fields=['username','password']


        
        
        
            
    
        
        