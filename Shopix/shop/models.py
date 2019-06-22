from django.db import models
from django.urls import reverse
from django.conf import settings 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    class Meta:
        verbose_name_plural = ("Categories")
        ordering = ('name',)
        verbose_name = 'Category'
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])
    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='uproducts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    photo = models.ImageField(upload_to='upload/%Y/%m/%d', unique=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id, self.slug])
    def __str__(self):
        return self.name

# class Image(models.Model):
#     product = models.ForeignKey(Product,related_name='images',  on_delete=models.CASCADE)
#     file = models.ImageField(upload_to='upload/%Y/%m/%d', unique=True)
#     position = models.PositiveSmallIntegerField(default=1)
#     class Meta:
#         ordering = ('position',)
#     def __str__(self):
#         return '{} - {}'.format(self.product.name, self.file)
