from django.shortcuts import render

from car.models import CarModel
from brand.models import BrandModel
# Create your views here.

def home(request, brand_slug = None):
    data = CarModel.objects.all()
    if brand_slug is not None:
        brand = BrandModel.objects.get(slug = brand_slug)
        data = CarModel.objects.filter(brand = brand)
        
    brand = BrandModel.objects.all()
    return render(request, 'home.html', {'data':data, 'brand': brand})