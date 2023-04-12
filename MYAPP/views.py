from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def background(request):
    return render(request,"textonimage.html")
def bills(request):
    return render(request,"biling.html")
def image(request):
    return render(request,"images.html")
def members(request):
    all=Student.objects.all().values()
    details={
        "members":all
         }
    return render(request,"members.html",details)
def Student(request):
    stud=StudentForm()
    return render(request,'student.html',{'form':stud})
def Employee(request):
    emp=EmployeeForm()
    return render(request,'employee.html',{'form':emp})
