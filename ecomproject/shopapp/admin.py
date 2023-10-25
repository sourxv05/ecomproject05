from django.contrib import admin

# Register your models here.
from . models  import product,Category

class categoryadmin(admin.ModelAdmin):
    list_display = ('name','slug','img')

    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,categoryadmin)



class productadmin(admin.ModelAdmin):
    list_display = ('name','slug','price','img','stock','available','created','updated','des','price2')
    list_editable = ('price','stock','available','img','des','price2')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,productadmin)






