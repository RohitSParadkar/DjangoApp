from django.shortcuts import render,HttpResponse

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
    return render(request,'contactUs.html')