from django.contrib import admin
from .models import Carousel, Category, SubCategory, Product, Review,ColorProduct,SizeProduct

# Register your models here.


admin.site.register(Carousel)
admin.site.register(Review)
admin.site.register(ColorProduct)
admin.site.register(SizeProduct)


class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name',]
    prepopulated_fields={'slug':('name',)}


class SubCategoryAdmin(admin.ModelAdmin):
    list_display= ['name',]
    prepopulated_fields={'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display= ['name',]
    prepopulated_fields={'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
