from django.db import models
from django.contrib.auth import get_user_model
from stores.models import Product


# Create your models here.

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=150, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    address2 = models.TextField(null=False, blank=False)
    city = models.CharField(max_length=150, null=False, blank=False)
    state = models.CharField(max_length=150, null=False, blank=False)
    zipcode = models.CharField(max_length=150, null=False, blank=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    message = models.TextField(null=True, blank=True)
    total_price = models.FloatField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    upadte_at = models.DateTimeField(auto_now=True)
    orderstatus = (
        ('pending', 'Pending'),
        ('out of shipping ', 'Out of Shipping'),
        ('complete', 'Complete'),
    )
    status = models.CharField(
        max_length=100, choices=orderstatus, default='pending')
    tracking_no = models.CharField(max_length=150, null=False)

    def __str__(self):
        return '%s %s' % (self.id, self.tracking_no)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    price = models.FloatField(null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return '%s %s' % (self.id, self.order.tracking_no)

