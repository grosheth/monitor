from django.shortcuts import render, HttpResponse
import api

# Create your views here.
def dashboard(request):
    return render(request, "controller/dashboard.html", context={"test": range(5)})

def pods(request):
    namelist = api.command("kubectl get pods --output name")
    print(list(namelist))
    number_of_pods = api.command("kubectl get pods --output name | wc -l")
    return render(request, "controller/pods.html", context={"length": int(number_of_pods), "namelist": list(namelist)})