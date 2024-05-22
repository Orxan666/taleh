from django import template

from ..models import Category ,GeneralCategory
from customer.models import WishItem
register = template.Library()

@register.inclusion_tag('includes/nav-categories.html')
def nav_category():
    pure_categories=Category.objects.filter(general_category__isnull=True)
    general_categories=GeneralCategory.objects.all()
    return{
        'pure_categories':pure_categories,
        'general_categories':general_categories,
    }



@register.filter
def is_wished(product,request):
    if not request.user.is_authenticated:
        return False
    return WishItem.objects.filter(product=product,customer=request.user.customer).exists()


@register.simple_tag

def get_querystring(request, key, value):
    querydict = request.GET.copy()
    querydict[key] = value
    querystring = querydict.urlencode()
    return '?' + querystring