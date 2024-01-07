from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from dashboard.forms import DiscountForm, ProductForm
from store.models import Discount, Product


# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def manage_store(request):
    return render(request, "dashboard/manage_store.html")


def list_user_products(request):
    products = Product.objects.filter(owner=request.user)
    context = {"products": products}
    return render(request, "dashboard/products.html", context=context)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully")
            return redirect("dashboard:user products")
        else:
            messages.error(request, "Product creation failed")
            return redirect("dashboard:add product")
    form = ProductForm()
    context = {"form": form}
    return render(request, "dashboard/product_form.html", context=context)


def update_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            if request.user != form.cleaned_data.get("owner"):
                messages.error(request, "UnAuthorized Request")
                return redirect("dashboard:add product")
            form.save()
            messages.success(request, "Product updated successfully")
            return redirect("dashboard:user products")
        else:
            messages.error(request, "Product updation failed")
            return redirect("dashboard:user products")
    product = Product.objects.get(pk=request.POST.get("id"))
    form = ProductForm(instance=product)
    context = {"form": form}
    return render(request, "dashboard/product_form.html", context=context)


def delete_product(request):
    if request.method == "POST":
        product_id = request.POST.get("id")
        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            messages.success(request, "Product deleted successfully")
        except Exception as e:
            messages.error(request, f"Unable to delete the Product {e}")
        return redirect("dashboard:user products")
    return HttpResponse("Bad Request", status=400)


def show_sales(request):
    context = {}
    return render(request, "dashboard/show_sales.html", context=context)


def list_discounts(request):
    discounts = Discount.objects.filter(product__owner=request.user)
    context = {"discounts": discounts}
    return render(request, "dashboard/discounts.html", context=context)


def add_discount(request):
    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Discount added successfully")
        else:
            messages.error(request, "Unable to add discount")
        return redirect("dashboard:user products")
    form = DiscountForm()
    context = {"form": form}
    return render(request, "dashboard/discount_form.html", context=context)


def update_discount(request):
    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Discount updated successfully")
        else:
            messages.error(request, "Unable to update discount")
        return redirect("dashboard:user discounts")
    discount = Discount.objects.get(pk=request.POST.get("id"))
    form = DiscountForm(instance=discount)
    context = {"discount": discount}
    return render(request, "dashboard/discount_form.html", context=context)


def delete_discount(request):
    if request.method == "POST":
        discount_id = request.POST.get("id")
        try:
            discount = Discount.objects.get(pk=discount_id)
            discount.delete()
            messages.success(request, "Discount deleted successfully")
        except Exception as e:
            messages.error(request, f"Unable to delete discount {e}")
        return redirect("dashboard:user discounts")
    return HttpResponse("Bad Request", status=400)
