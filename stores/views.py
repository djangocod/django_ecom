from django.contrib import messages
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Carousel, Category, ColorProduct, Product, SizeProduct, SubCategory, Review
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.


def store_home(request):
    carousel = Carousel.objects.filter().first()
    category = Category.objects.all()
    context = {
        'carousel': carousel,
        'category': category,

    }
    return render(request, 'stores/index.html', context)


def store_shopping(request):
    products = Product.objects.all().order_by('?')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    context = {
        'products': page,

    }
    return render(request, 'stores/shope.html', context)


def store_category_product(request, slug_cate):
    category = get_object_or_404(Category, slug=slug_cate)
    print(category)
    products = Product.objects.filter(category=category).order_by('?')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    context = {
        'products': page,
        'cat': category,

    }
    return render(request, 'stores/shopping_cate.html', context)


def store_product_details(request, pro_slug):

    product = get_object_or_404(Product, slug=pro_slug)
    products = Product.objects.filter(category=product.category).exclude(
        name=product.name).order_by('?')
    reviews = Review.objects.filter(product=product)
    paginator = Paginator(reviews, 2)
    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    product = Product.objects.get(slug=pro_slug)
    author = request.user
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        review = request.POST.get('review')
        rating_view = request.POST.get('rating')
        if author.is_authenticated:
            if Review.objects.filter(product=product, author=author).first():
                messages.error(
                    request, ' You Already Have a Reviews on This Product ')
                return redirect(url)
            if rating_view and review:
                rev = Review(
                    product=product,
                    review=review,
                    author=author,
                    rating=rating_view,
                )
                rev.save()
                review = ''
                rating_view = ''
                messages.success(request, 'Thank You ')

            else:
                messages.error(request, ' Please Rate and Text To Reviews ')
        else:
            messages.success(request, 'you must logged in')
            return redirect(url)

    all_review_count = Review.objects.filter(product=product).count()
    size = SizeProduct.objects.all()
    context = {
        'product': product,
        'products': products,
        'reviews': page,
        'all_review_count': all_review_count,
        'size':size

    }
    return render(request, 'stores/product_detail.html', context)


def store_sub_menu_product(request, cat_slug):
    sub_categorey = get_object_or_404(SubCategory, slug=cat_slug)
    product = Product.objects.filter(subcategory=sub_categorey).order_by('?')
    paginator = Paginator(product, 6)
    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    context = {
        'products': page,
        'sub_cat': sub_categorey
    }
    return render(request, 'stores/sub_menu_product.html', context)


def product_search(request):
    search = request.GET.get('search_store')
    search_pro = Product.objects.filter(name__icontains=search)
    paginator = Paginator(search_pro, 6)
    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    context = {'search_pro': page, 'search': search}
    return render(request, 'stores/search_results.html', context)
