from django.shortcuts import render,HttpResponse

# Create your views here.

def Homepage(request):
    return render(request,'Homepage.html')

def product(request):
     return render(request,'product.html')
def About(request):
     return render(request,'About.html')

def Contuct(request):
     return render(request,'Contuct.html')
