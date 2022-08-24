from os import sep
from unicodedata import name
from django.shortcuts import render, HttpResponse
import api

# Create your views here.
def dashboard(request):
    return render(request, "controller/dashboard.html", context={"test": range(5)})

def pods(request):
    namelist = api.command("kubectl get pods --output name")
    number_of_pods = api.command("kubectl get pods --output name | wc -l")
    separated = namelist.split("\n")
    
    if len(separated) > int(number_of_pods):
        separated.pop(-1)
        
    return render(request, "controller/pods.html", context={"length": range(int(number_of_pods)), "namelist": separated})