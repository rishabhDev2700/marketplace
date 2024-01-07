from django.urls import path

from dashboard.seller_views import (
    add_discount,
    add_product,
    dashboard,
    delete_discount,
    delete_product,
    list_discounts,
    list_user_products,
    manage_store,
    show_sales,
    update_discount,
    update_product,
)

# Create your models here.
app_name = "dashboard"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("/sales", show_sales, name="sales"),
    path("/manage-store", manage_store, name="manage-store"),
    path("/list-my-products", list_user_products, name="user products"),
    path("/add-product", add_product, name="add product"),
    path("/update-product", update_product, name="update product"),
    path("/delete-product", delete_product, name="delete product"),
    path('/list-discounts', list_discounts, name="user discounts"),
    path("/add-discount", add_discount, name="add discount"),
    path("/update-discount", update_discount, name="update discount"),
    path("/delete-discount", delete_discount, name="delete discount"),
]
