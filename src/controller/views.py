from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, "controller/dashboard.html", context={"test": range(5)})

def pods(request):
    return render(request, "controller/pods.html", context={"test": range(5)})