from django.shortcuts import render
from .models import Category, Place
# Create your views here.
def home(request):
    categories = Category.objects.all()
    return render(request, "home.html", {"categories": categories})

def category(request, categoryid):
    categories = Category.objects.all()
    places = Place.objects.filter(category = categoryid)
    return render(request, "category.html", {"categories": categories, "places": places})        