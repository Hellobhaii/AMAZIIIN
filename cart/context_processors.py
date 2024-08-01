from .cart import Cart

# create context processors
def cart(request):
    return {'cart': Cart(request)}