from django.shortcuts import render

def index(request):
    return render(request, "landing/index.html")

def about_us(request):
    return render(request, "landing/about.html")