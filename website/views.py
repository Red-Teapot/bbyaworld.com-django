from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'website/index.html')

def rules(request):
    return render(request, 'website/rules.html')

def newbie_info(request):
    return render(request, 'website/newbie-info.html')