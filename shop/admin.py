from django.contrib import admin

# Register your models here.
from .models import Size,Color,GeneralCategory,Category,Campaign,Product,ProductImage

class ProductImageInline(admin.TabularInline):
    model=ProductImage
    readonly_fields=['image_tag']
    extra=1
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageInline]
    list_filter = ['categories']


admin.site.register(Size)
admin.site.register(Color)
admin.site.register(GeneralCategory)
admin.site.register(Category)
admin.site.register(Campaign)
admin.site.register(ProductImage)