from django.shortcuts import render
from .models import Product, Category, Brand

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.object.all()

    context = {
        "products": products,
        "categories": categories,
        "brands": brands
        }
    return render(request, "app/index.html")
