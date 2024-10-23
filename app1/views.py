from django.shortcuts import render

def index(request):
    return render(request, 'app1/index.html')

def login(request):
    return render(request, 'app1/login.html')

def about(request):
    return render(request, 'app1/about.html')
