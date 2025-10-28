from django.shortcuts import render
from app.models import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    category = Category.objects.all()
    brand =    Brand.objects.all()

    context = {
        "products":products,
        "category":category,
        "brand":brand
    }
    return render(request,"app/index.html", context=context)