from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from profiles.models import Profile

User = get_user_model()

# Create your models here.


class Category(models.Model):
    slug = models.SlugField(max_length=200, unique=True,
                            null=False, blank=False)
    name = models.CharField(max_length=200, unique=True,
                            null=False, blank=False)
    category_image = models.ImageField(
        upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.category_image.delete()
        return super().delete(*args, **kwargs)


class Carousel(models.Model):
    carousel_image1 = models.ImageField(upload_to='carousel')
    carousel_image2 = models.ImageField(upload_to='carousel')

    def delete(self, *args, **kwargs):
        self.carousel_image.delete()
        return super().delete(*args, **kwargs)


class SubCategory(models.Model):
    sub_category = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class SizeProduct (models.Model):
    slug = models.SlugField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.name


class ColorProduct (models.Model):
    slug = models.SlugField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    


    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True,
                            null=False, blank=True)
    name = models.CharField(max_length=200, unique=True,
                            null=False, blank=False)
    color = models.CharField(max_length=200)
                            
    product_image = models.ImageField(
        upload_to='product', null=False, blank=False)
    product_img1 = models.ImageField(
        upload_to='product/sub', null=True, blank=True)
    product_img2 = models.ImageField(
        upload_to='product/sub', null=True, blank=True)
    product_img3 = models.ImageField(
        upload_to='product/sub', null=True, blank=True)
    product_quantity = models.IntegerField()
    current_price = models.FloatField()
    selling_price = models.FloatField()
    small_description = models.TextField(
        max_length=500, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    information = models.TextField(max_length=500, null=False, blank=False)
    product_size = models.ManyToManyField(
        SizeProduct, related_name='product_size')
    product_color = models.ManyToManyField(
        ColorProduct, related_name='product_color')
    

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.product_image.delete()
        self.product_img1.delete()
        self.product_img2.delete()
        self.product_img3.delete()
        return super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("stores:product_search", args=[self.name])


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    review = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.review
