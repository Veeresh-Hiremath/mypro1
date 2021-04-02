from django.shortcuts import render
def index(request):
    return render(request,"sample.html")
def index2(request):
    return render(request,"sample2.html")
# Create your views here.
