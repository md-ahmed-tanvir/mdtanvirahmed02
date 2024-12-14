from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Contract

# Create your views here.

def dashboard(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contract(request):
    if request.method == "POST":  # Corrected the typo here
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        values = Contract(name=name,email=email, desc=desc)
        values.save()
    return render(request, 'contract.html')



