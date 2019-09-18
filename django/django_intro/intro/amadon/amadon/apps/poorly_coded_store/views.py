from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    recent_transaction= Order.objects.last()
    context = {
                'quantity': recent_transaction.quantity_ordered,
                'total_price': recent_transaction.total_price
                    }
    return render(request, "store/checkout.html",context)


# 1) create a redirect route so the DB is not charged after every refresch redirect to checkout

def process_order(request):
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(request.POST["price"])
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect('/checkout')
