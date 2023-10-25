from django.db import models

# Create your models here.
from shopapp.models import product

class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date=models.DateField(auto_now_add=True)


    class Meta:
        db_table='Cart'
        ordering=['date']
    def __str__(self):
        return '{}'.format(self.cart_id)

class Cartitem(models.Model):
    Product=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)



    class Meta:
        db_table='Cartitem'
    def sub_total(self):
        return self.Product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.Product)
