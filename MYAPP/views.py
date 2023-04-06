from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def background(request):
    return render(request,"textonimage.html")
