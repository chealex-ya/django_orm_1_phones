from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort")
    phones = Phone.objects.all()
    if 'name' == sort:
        phones = Phone.objects.order_by('name')
    if 'min_price' == sort:
        phones = Phone.objects.order_by('price')
    if 'max_price' == sort:
        phones = Phone.objects.order_by('-price')
    context = {
        'phones' : phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug = slug)
    context = {
        'phone' : phone
    }
    return render(request, template, context)
