from django.shortcuts import render
from item.models import Category, Item


# Create your views here.
def home(request):
    categories = Category.objects.all()[0:6]
    items = Item.objects.filter(is_sold=False)
    return render(request, "core/Home.html", {"items": items, "categories": categories,})
