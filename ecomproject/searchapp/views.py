from django.shortcuts import render

# Create your views here.
from shopapp.models import product
from django.db.models import Q
from django.views.generic import ListView
from .models import Review


def search(request):
    products=None
    query=None
    if 'q' in request.GET:
        query= request.GET.get('q')
        products=product.objects.all().filter(Q(name__contains=query) | Q(des__contains=query))
    return render(request,'search.html',{'query':query,'products':products})


# # def review(request):
# #     t2=Review.objects.all()
# #     if request.method=='POST':
# #         name=request.POST.get('name','')
# #         # product=request.POST.get('product','')
# #         review=request.POST.get('review','')
# #         t1=Review(name=name,review=review)
# #         t1.save()
# #     return render(request,'product.html',{'t2':t2})
# class view(ListView):
#     model=Review
#     template_name = 'product.html'
#     context_object_name = 't2'
