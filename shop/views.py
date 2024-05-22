from django.shortcuts import render,get_object_or_404
from .models import Campaign,Product,Category,Size,Color
from django.db.models import Count
from django.core.paginator import Paginator
from .filters import ProductFilter
# Create your views here.

def home(request):

    slide_campaigns=Campaign.objects.filter(is_slide=True)[:3]
    nonslide_campaigns=Campaign.objects.filter(is_slide=False)[:4]
    categories=Category.objects.annotate(product_count=Count('products'))
    featured_products=Product.objects.filter(featured=True)[:8]
    recent_products=Product.objects.all().order_by('-created')[:8]
    return render(request,'home.html',{
        'slide_campaigns':slide_campaigns,
        'nonslide_campaigns':nonslide_campaigns,
        'categories':categories,
        'featured_products':featured_products,
        'recent_products':recent_products
    })


def product_list(request):
    products=Product.objects.all()
    search_input = request.GET.get('search')

    if search_input:
        # products=products.filter(title=search_input)
        # products=products.filter(title__iexact=search_input)
        products=products.filter(title__icontains=search_input)

    sorting_input=request.GET.get('sorting')
    if sorting_input:
        products=products.order_by(sorting_input)






    product_filter=ProductFilter(request.GET,queryset=products)
    products=product_filter.qs

    page_by_input=int(request.GET.get('page_by',3))
    page_input=request.GET.get('page',1)
    paginator=Paginator(products,page_by_input)

    try:
        page=paginator.page(page_input)
        products=page.object_list
    except:
        page = paginator.page(1)
        products = page.object_list


    colors=Color.objects.all().annotate(product_count=Count('products'))
    sizes=Size.objects.all().annotate(product_count=Count('products'))



    return render(request,'product-list.html',{
        "products":products,
        'paginator':paginator,
        'page':page,
        'sizes':sizes,
        'colors':colors,
    })



def product_detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
    other_products=Product.objects.exclude(pk=product.pk).order_by('?')[:5]
    return render(request,'product-detail.html',{
        'product':product,
        'other_products':other_products,
    })