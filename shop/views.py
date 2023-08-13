from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Contact
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

    cats = {item['category'] for item in catProds}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        allProds.append([prod, range(1, slides), slides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html',  params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    message = ""
    if request.method == "POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email,

                          phone=phone,
                          address=address,
                          desc=desc)
        contact.save()
        message = "We will contact you " + name
        params = {'message': message}
    return render(request,  'shop/contact.html', {'message': message})


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return HttpResponse('THis sis search page')


def productView(request, id):
    product = Product.objects.filter(id=id)
    print(product)
    return render(request, 'shop/prodView.html', {'product': product[0]})


def checkout(request):
    return HttpResponse('THis si check out page')
