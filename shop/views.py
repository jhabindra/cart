from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):

    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse('This is contact')


def tracker(request):
    return HttpResponse('THis is tracker page')


def search(request):
    return HttpResponse('THis sis search page')


def productView(request):
    return HttpResponse('THis is productview Page')


def checkout(request):
    return HttpResponse('THis si check out page')
