from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard(request):
    return HttpResponse("<h1>Dashboard pour Kubernetes</h1>")