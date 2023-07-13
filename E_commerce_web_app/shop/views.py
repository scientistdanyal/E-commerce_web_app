from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse('this is contact')

def traker(request):
    return HttpResponse('this is traker')

def search(request):
    return HttpResponse('this is search')



def productView(reques):
    return HttpResponse('this is product view')

def checkout(request):
    return HttpResponse('this is checkout')