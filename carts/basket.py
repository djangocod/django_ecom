
from stores.models import Product



class Basket:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in self.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add_to_cart(self, product, qty):
        pro_id = str(product.id)
        if pro_id not in self.cart:
            self.cart[pro_id] = {'qty': qty, 'price': float(product.selling_price)}

        self.session.modified = True


    def add_to_cart_mulitply(self, product, qty=1):
        pro_id = str(product.id)

        if pro_id not in self.cart:
            self.cart[pro_id] = {'qty': qty, 'price': float(product.selling_price)}
        else:
            self.cart[pro_id]['qty'] = qty

        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())    

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids) 

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['total_sub_price'] = item['price']*item['qty']
            yield item
           


    def total_price(self):
        total = sum(item['total_sub_price'] for item in self.cart.values())
        return total

    def clear_cart(self):
        del self.session['skey']
        self.session.modified =True

    def delete_product(self,product):
        pro_id = str(product.id)
        if pro_id in self.cart:
            del self.cart[pro_id]
            self.session.modified = True
