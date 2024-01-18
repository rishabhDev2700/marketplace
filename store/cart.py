from decimal import Decimal

from store.models import Product


class Cart:
    def __init__(self, request) -> None:
        self.session = request.Session
        cart = self.session.get("cart")
        if ...:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id] = {"price": product.price, "quantity": quantity}
        self.save()

    def save(self):
        self.session.modified = True

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        # todo: complete constructor and clear()

    def clear(self):
        del self.session

    def __len__(self):
        return sum(product["quantity"] for product in self.cart.values())

    def subtotal(self):
        return sum(
            Decimal(product["price"]) * product["quantity"] for product in self.cart
        )

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.pk)]["product"] = product
        for product in cart.values():
            product["total_price"] = product["price"] * product["quantity"]
            yield product
