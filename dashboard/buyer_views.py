"""Views functions for buyers"""


from django.shortcuts import render
from store.models import Order, OrderProduct


def buyer_history(request):
    orders = Order.objects.filter(user=request.user)
    orders_history = []
    for order in orders:
        products = OrderProduct.objects.filter(order=order)
        each_order = {"order": order, "products": products}
        orders_history.append(each_order)
    context = {"orders_history": orders_history}
    return render(request,'dashboard/history.html',context=context)


