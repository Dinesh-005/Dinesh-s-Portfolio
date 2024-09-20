from django.shortcuts import render
from django.http import HttpResponse
from .models import data

def home(request):
    return render(request,'home.html')
def education(request):
    return render(request,'education.html')
def services(request):
    return render(request,'services.html')
def projects(request):
    return render(request,'projects.html')
def contactform(request):
    return render(request,'contactform.html')
 
def contact(request):
  if request.method=="POST":
     name1=request.POST["name"]
     email1=request.POST["email"]
     contactno1=request.POST["contactno"]
     subject1=request.POST["subject"]
     message1=request.POST["message"]

     context={
       
         'user':name1,
         'mail':email1,
         'no':contactno1,
         'sub':subject1,
         'msg':message1
     }
     obj=data()

     obj.name=name1,
     obj.email=email1,
     obj.contactno=contactno1,
     obj.subject=subject1,
     obj.message=message1,
     obj.save()

     return render(request,'home.html',context)


