from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .basket import Basket
from stores.models import Product
from profiles.models import Profile
import random
from django.contrib.auth import get_user_model
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.

user = get_user_model()


def cart_view(request):
    return render(request, 'carts/cart_view.html')


def cart_add_product(request):
    cart = Basket(request)
    if request.method == 'POST':
        prod = int(request.POST['product_id'])
        product = Product.objects.get(id=prod)
        cart.add_to_cart(product=product, qty=1)
        cart_qty_total = cart.__len__()
    return JsonResponse({'status': 'added to basket successfully', 'cart_qty_total': cart_qty_total})


def cart_add_product_from_detail(request):
    cart = Basket(request)
    if request.method == 'POST':
        pro_id = int(request.POST['product_id'])
        pro_qty = int(request.POST['product_qty'])
        product = Product.objects.get(id=pro_id)

        if product.product_quantity >= pro_qty > 0:
            cart.add_to_cart_mulitply(product=product, qty=pro_qty)
            response = 'updated Quantity of basket successfully'
            cart_qty_total = cart.__len__()
        else:
            response = 'This Quantity Out Of Stock'
    return JsonResponse({'status': response, 'cart_qty_total': cart_qty_total})


def update_cart(request):
    cart = Basket(request)
    if request.method == 'POST':
        pro_id = int(request.POST['product_id'])
        pro_qty = int(request.POST['product_qty'])
        product = Product.objects.get(id=pro_id)

        if product.product_quantity >= pro_qty > 0:
            cart.add_to_cart_mulitply(product=product, qty=pro_qty)
            response = 'updated Quantity of basket successfully'
            cart_qty_total = cart.__len__()
        else:
            cart.delete_product(product=product)
            response = 'removed from basket successfully'
            cart_qty_total = cart.__len__()

    return JsonResponse({'status': response, 'cart_qty_total': cart_qty_total})


def delete_cart_item(request):
    cart = Basket(request)
    if request.method == 'POST':
        pro_id = int(request.POST['product_id'])
        product = Product.objects.get(id=pro_id)
        cart.delete_product(product=product)
        cart_qty_total = cart.__len__()
        response = 'Removed Product of basket successfully'
    return JsonResponse({'status': response, 'cart_qty_total': cart_qty_total})


@login_required(login_url='users:account_login')
def checkout_cart(request):
    cart = Basket(request)

    if request.method == 'POST':
        current_user = user.objects.filter(id=request.user.id).first()
        if not current_user.first_name:
            current_user.first_name = request.POST['fname']
            current_user.last_name = request.POST['lname']
            current_user.save()
        if not Profile.objects.filter(user=current_user):
            profile = Profile()
            profile.email = request.POST['email']
            profile.phone = request.POST['phone']
            profile.address = request.POST['address']
            profile.adress2 = request.POST['adress2']
            profile.state = request.POST['state']
            profile.city = request.POST['city']
            profile.zipcode = request.POST['zipcode']
            profile.save()
        neworder = Order()
        neworder.user_id = request.user.id
        neworder.email = request.POST['email']
        neworder.phone = request.POST['phone']
        neworder.address = request.POST['address']
        neworder.address2 = request.POST['address2']
        neworder.state = request.POST['state']
        neworder.city = request.POST['city']
        neworder.zipcode = request.POST['zipcode']
        neworder.payment_mode = request.POST['payment_mode']
        track_no = 'site' + str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_no=track_no) is None:
            track_no = 'site' + str(random.randint(1111111, 9999999))
        neworder.tracking_no = track_no
        total = 0
        for item in cart:
            total = total + item['total_sub_price']
        if cart.__len__() > 0:
            neworder.total_price = total
            neworder.save()
            for item in cart:
                OrderItem.objects.create(
                    order=neworder,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['qty']
                )
                order_product = Product.objects.filter(name=item['product']).first()
                order_product.product_quantity = order_product.product_quantity - item['qty']
                order_product.save()
            cart.clear_cart()
            messages.success(request, 'order placed')
        else:
            messages.success(request, 'cart is empty')
    return redirect('/')


@login_required(login_url='users:account_login')
def place_order_cart(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {'profile': profile, 'user': user}
    return render(request, 'carts/placeorder.html', context)
