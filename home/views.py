from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contacts
contextText = {
     'title':'CryptoWeb'
}

# Create your views here.
def index(request):
    return render(request,'index.html',contextText)
    # return HttpResponse('this is home')

def about(request):
    return render(request,'aboutUs.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    #logic for form submission
    if request.method=='POST':
        id = request.POST.get("id")
        email = request.POST.get("email") #get email from dictionary of post 
        message = request.POST.get("message")
        contact = Contacts(email=email,message=message,date=datetime.today())#save above extracted values in database
        contact.save()
    return render(request,'contactUs.html')