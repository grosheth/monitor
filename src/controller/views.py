from django.shortcuts import render, HttpResponse
import controller

# Create your views here.
def dashboard(request):
    return render(request, "controller/dashboard.html", context={"test": range(5)})

def pods(request):
    namelist = list(controller.command("kubectl get pods --output name"))
    number_of_pods = controller.command("kubectl get pods --output name | wc -l")
    return render(request, "controller/pods.html", context={"length": number_of_pods, "namelist": namelist})