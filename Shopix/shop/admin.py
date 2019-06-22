from django.contrib import admin
from . models import Product, Category#, Image

#Register your models here.


# class ImageInline(admin.StackedInline):
#     model = Image
#     extra = 1
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'slug', 'category','price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    # inlines = [ImageInline]
    # def save_model(self, request, obj, form, change):
    #     super(ProductAdmin,self).save_model(request, obj, form, change)
    #     obj.save
    #     for afile in request.FILES.getlist('photos_multiple'):
    #         obj.images.create(file=afile)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
#admin.site.register(Image)
