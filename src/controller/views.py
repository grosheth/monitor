from django.shortcuts import render, HttpResponse
import api

# Create your views here.
def dashboard(request):
    return render(request, "controller/dashboard.html", context={"test": range(5)})

def pods(request):
    namelist = api.command("kubectl get pods --output name")
    print(namelist)
    print(type(namelist))
    number_of_pods = api.command("kubectl get pods --output name | wc -l")
    print(number_of_pods)
    print(type(number_of_pods))
    return render(request, "controller/pods.html", context={"length": number_of_pods, "namelist": namelist})