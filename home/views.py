from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contacts
from django.contrib import messages
contextText = {
     'title':'CryptoWeb'
}

# Create your views here.
def index(request):
    #messages.success(request, "Profile details updated.")
    return render(request,'index.html',contextText)
    # return HttpResponse('this is home')

def about(request):
    return render(request,'aboutUs.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    #make migrations: create changes
    #logic for form submission
    if request.method=='POST':
        id = request.POST.get("id")
        email = request.POST.get("email") #get email from dictionary of post 
        message = request.POST.get("message")
        contact = Contacts(email=email,message=message,date=datetime.today())#save above extracted values in database
        contact.save()
        messages.success(request, "Form Successfully Submited")
    return render(request,'contactUs.html')