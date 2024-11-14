import requests
from django.shortcuts import render
from django.core.paginator import Paginator

def home(request):
    # Fetch products from the API
    response = requests.get('https://fakestoreapi.com/products')
    products = response.json()
    
    # Set up pagination
    items_per_page = 5
    paginator = Paginator(products, items_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'store/home.html', {
        'page_obj': page_obj,
    })