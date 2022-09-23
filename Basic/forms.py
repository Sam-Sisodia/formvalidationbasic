
from django import forms
from . models import *

class UserRegistarionForm(forms.Form):
    firstname = forms.CharField(error_messages={'required': 'Enter your name pls'})
    lastname = forms.CharField()
    gender = forms.CharField()
    email =forms.EmailField()
    password = forms.CharField()
    


    # class Meta:
    #     model = UserRegister
    #     fields = ['firstname','lastname','email','gender','password']
        
        
        

    def clean_firstname(self):
        valfirstname = self.cleaned_data['firstname'] 
        if len(valfirstname)<4:
            raise forms.ValidationError("Eneter more then or equal to 4 charecter")

        return valfirstname

    def clean_email(self):    
        validateemail = self.cleaned_data['email']
        if UserRegister.objects.filter(email=validateemail).exists():
            raise forms.ValidationError("Email already exist")
        return validateemail 

        




    
    







'''
class UserRegistarionForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    gender = forms.BooleanField()
    email =forms.EmailField()
    password = forms.CharField()

    def clean_firstname(self):
        valfirstname = self.cleaned_data['firstname'] 
        if len(valfirstname)<4 or valfirstname == "":
            raise forms.ValidationError("Eneter more then or equal to 4 charecter")
        return valfirstname

    def clean_email(self):
        validateemail = self.cleaned_data['email']
        if UserRegister.objects.filter(email=validateemail).exists():
            raise forms.ValidationError("Email already exist")
        return validateemail 




'''