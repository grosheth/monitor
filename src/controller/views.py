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

def deployment(request):
    namelist = api.command("kubectl get deploy --output name")
    number_of_deploy = api.command("kubectl get deploy --output name | wc -l")
    separated = namelist.split("\n")
    
    if len(separated) > int(number_of_deploy):
        separated.pop(-1)
        
    return render(request, "controller/deployment.html", context={"length": range(int(number_of_deploy)), "namelist": separated})

def services(request):
    namelist = api.command("kubectl get service --output name")
    number_of_services = api.command("kubectl get pods --output name | wc -l")
    separated = namelist.split("\n")
    
    if len(separated) > int(number_of_services):
        separated.pop(-1)
        
    return render(request, "controller/services.html", context={"length": range(int(number_of_services)), "namelist": separated})

def info(request, resource, name):
    info_pod = api.command(f"kubectl describe pod { name }")
    info_deployment = api.command(f"kubectl describe deploy { name }")
    info_service = api.command(f"kubectl describe service { name }")

    if resource == "pod":
        separated = info_pod.split("\n")
        resource_type = "Pod"
    elif resource == "deployment.apps":
        separated = info_deployment.split("\n")
        resource_type = "Deployment"
    else:
        separated = info_service.split("\n")
        resource_type = "Service"

    return render(request, "controller/info.html", context={"info": separated, "resource_type": resource_type})