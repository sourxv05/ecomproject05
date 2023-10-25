from django.db import models

# Create your models here.
from shopapp.models import product

class Review(models.Model):
    name=models.CharField(max_length=150)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    review=models.TextField()
