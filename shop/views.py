from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from math import ceil


# Create your views here.


def index(request):
    products = Product.objects.all()

    n = len(products)
    slides = n//4 + ceil(n/4-(n//4))
    # params = {'no_of_slide': slides, 'range': range(
    #     1, slides), 'productlist': products}
    # allProds = [[products, range(1, slides), slides], [
    #     products, range(1, slides), slides]]
    allProds = []
    catProds = Product.objects.values('category', 'id')
    print(catProds)
    cats = {item['category'] for item in catProds}
    print(cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        allProds.append([prod, range(1, slides), slides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html',  params)


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
