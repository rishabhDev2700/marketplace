"""This file contains all view functions related to store"""
from django.shortcuts import render, get_object_or_404

from store.models import Category, Product


# Create your views here.
def homepage(request):
    """
    Home page of the website
    """
    new_arrivals = Product.objects.all()[:10]
    context = {"new_arrivals": new_arrivals}
    return render(request, "store/homepage.html", context=context)


def list_all(request):
    """
    Shows all products available
    """
    # todo: add pagination
    products = Product.objects.filter(is_available=True)
    context = {"products": products}
    return render(request, " stores/list-all.html", context=context)


def show_product(request, slug):
    """Show a particular product"""
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    return render(request, "store/show-product.html", context=context)


def list_categories(request):
    """
    Shows the list of categories
    """
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "store/list-categories.html", context=context)


def show_category(request, slug):
    """Shows all products in the given category"""
    products = Product.objects.filter(category=slug)
    context = {"products": products}
    return render(request, "store/show-category.html", context=context)


def list_best_sellers(request):
    """Fetches the bestsellers"""
    return render(request, "store/list-best-sellers.html")


def list_new_arrivals(request):
    """Fetches the new arrivals from the database"""
    return render(request, "store/list-new-arrivals.html")
