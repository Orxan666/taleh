from django.urls import path,include
from . import views

app_name='shop'
urlpatterns = [
      path('i18n/', include('django.conf.urls.i18n')),
    path('',views.home,name='home'),
    path('products',views.product_list,name='product-list'),
    path('products/<int:pk>/',views.product_detail,name='product-detail'),
]
