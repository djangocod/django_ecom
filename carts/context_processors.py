from carts.basket import Basket

def cart(request):
    return {'cart': Basket(request)}