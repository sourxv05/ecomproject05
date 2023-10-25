from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    des=models.TextField(blank=True)
    img=models.ImageField(upload_to='category',blank=True)

    class meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_pulural='categories'
    def get_url(self):
        return reverse('shopapp:product_by_cate',args=[self.slug])

    def __str__(self):

        return '{}'.format(self.name)


class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    des=models.TextField(blank=True)
    img=models.ImageField(upload_to='product',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    price2=models.DecimalField(max_digits=10,decimal_places=2)
    def get_url(self):
        return reverse('shopapp:prodetail',args=[self.category.slug,self.slug])


    class meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_pulural='products'
    def __str__(self):
        return self.name
