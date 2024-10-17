from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to chai and django : Home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Welcolme to chai aur Django : About page")

def contact(request):
    return HttpResponse("Welcome to chai aur django : contact page")