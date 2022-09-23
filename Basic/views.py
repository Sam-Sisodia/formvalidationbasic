from distutils.log import error
from operator import ge
from types import NoneType
from django.shortcuts import render,HttpResponse

from  . forms import *
from .  models import *
# Create your views here.
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def home(request):
    return render(request, "index.html")


def register(request):
    if  request.method == "POST":
        form = UserRegistarionForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = request.POST.get('email')
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']
            
            user  = UserRegister.objects.create(firstname=firstname,lastname=lastname,email=email,gender=gender,password=password)                 #form.cleaned_data'['name']
            user.password = make_password('password') 
            user.save()
            messages.success(request,"Account Created Sucessfully")   
        else:
            form = UserRegistarionForm(request.POST)
            content = {'form':form};
            return render(request ,"register.html",content)

        
    return render(request ,"register.html")








# else:
#             form=UserRegistarionForm(request.POST)
#             return render(request,"register.html", locals(),)

#             #return HttpResponse("Form is Submitted")   


















































'''firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']'''





'''
if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            gender = forms.cleaned_data['gender']  
            user  = UserRegister.objects.create(firstname=firstname,lastname=lastname,email=email,gender=gender,password=password)                 #form.cleaned_data'['name']
            user.set_password(user.password)
            user.save()
            return HttpResponse("Form is Submitted")
                
    
    
    
    '''




'''

     firstname = form.cleaned_data['firstname']
            gender = request.POST.get('gender')
            user =UserRegister.objects.create(firstname=firstname,gender=gender)
            user.save()
            return HttpResponse("Form is Submitted")
    
    
    
    '''



    #  firstname = form.cleaned_data['firstname']
    #         lastname = form.cleaned_data['lastname']
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         print(password)
    #         gender = request.POST.get('gender')
    #         print(gender)
           
    #         user  = UserRegister.objects.create(firstname=firstname,lastname=lastname,email=email,gender=gender,password=password)                 #form.cleaned_data'['name']
    #         user.password = make_password('password') 
    #         user.save()











    #===================

'''
def register(request):
    if  request.method == "POST":
        form = UserRegistarionForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            gender = request.POST.get('gender')  
            user  = UserRegister.objects.create(firstname=firstname,lastname=lastname,email=email,gender=gender,password=password)                 #form.cleaned_data'['name']
            user.password = make_password('password') 
            user.save()
            messages.success(request,"Account Created Sucessfully")
            # return HttpResponse("Form is Submitted")       
    else:
        form = UserRegistarionForm()
    return render(request ,"register.html",{'form':form})
'''








'''

def register(request):
    if  request.method == "POST":
        form = UserRegistarionForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = request.POST.get('email')
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']
            print(gender)
            if gender =="Male":
                gender = True
            else:
                gender= False
            user  = UserRegister.objects.create(firstname=firstname,lastname=lastname,email=email,gender=gender,password=password)                 #form.cleaned_data'['name']
            user.password = make_password('password') 
            user.save()
            messages.success(request,"Account Created Sucessfully")   
        else:
            form = UserRegistarionForm(request.POST)
            content = {'form':form};
            return render(request ,"register.html",content)

        
    return render(request ,"register.html")







'''