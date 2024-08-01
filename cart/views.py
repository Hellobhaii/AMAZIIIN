from django.shortcuts import redirect, render, get_object_or_404
from .cart import Cart
from item.models import Item
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from.forms import PaymentForm
from.models import Order
from.forms import CheckoutForm

def cart_summary(request):
    cart = Cart(request)
    cart_items = cart.get_items
    quantities = cart.get_quants
    form = CheckoutForm()  
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_items":cart_items , "quantities":quantities, "form": form, "totals" : totals})  

def cart_add(request):
    if request.method == 'POST' and request.user.is_authenticated:
        cart = Cart(request)
        item_id = int(request.POST.get('item_id'))
        item_qty = int(request.POST.get('item_qty'))
        item = get_object_or_404(Item, id=item_id)
        cart.add(item=item, quantity=item_qty)
        cart_quantity =cart.__len__()
        return JsonResponse({'qty': cart_quantity})
        
        
        # return JsonResponse({'item_name': item.name})
    return HttpResponseForbidden()
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('item_id'))   
        cart.delete(item= item_id)
        response = JsonResponse({'item': item_id})
        return response



def cart_update(request):
    cart = Cart(request)
    if request.method == 'POST' and request.user.is_authenticated:
        
        item_id = int(request.POST.get('item_id'))
        item_qty = int(request.POST.get('item_qty'))
    cart.update(item= item_id, quantity = item_qty)
    response = JsonResponse({'qty': item_qty})
    return response


from.forms import CheckoutForm, PaymentForm
from.models import Order

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('cart:payment', order_id=order.id)
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

def payment(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process payment here
            #...
            return redirect('cart:payment_success')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form, 'order': order})



def payment_success(request):
    return render(request, 'payment_success.html')



