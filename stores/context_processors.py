
from .models import Category, SubCategory


def store_context_processors_category(request):
    sub_list = SubCategory.objects.all()
    category = Category.objects.all()

    return {
        'category_context': category,
        'subcategory_context': sub_list,
    }
