
from django.urls import path


from . import views
app_name='shopapp'

urlpatterns = [
      path('', views.allproduct,name='allproduct'),
      path('<slug:c_slug>/',views.allproduct,name='product_by_cate'),
       path('<slug:c_slug>/<slug:p_slug>/',views.prodetail,name='prodetail'),



]
