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
def Employee(request):
  if request.method=='post':
      form=EmployeeForm(request.post)
      if form.is_valid():
          form.save()
          return redirect("/")
  else :
      form=EmployeeForm()
      return render(request,'employee.html',{'form':form})

def setsession(request):
    request.session['firstname']='Laurine'
    request.session['lastname']='Maina'
    request.session['Email']='mainalaureen58@gmail.com'
    return HttpResponse('Session has been successfully created')
def getsession(request):
    fname=request.session['firstname']
    lname=request.session['lastname']
    emailaddress= request.session['Email']
    return HttpResponse(fname+' '+lname+' '+emailaddress)

def form(request):
    return render (request,"form.html")

def forms(request):
    return render (request,"form2.html")
