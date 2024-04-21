from django.contrib import admin
from .models import *

admin.site.site_header = 'FARM LINK '


class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'category', 
                    'packaging', 'harvest_date', 'cost_price', 'Shelf_life', 'date_added',)
    list_filter = ('category',)
    fields = ('name', 'origin', 'category', 
                    'packaging', 'harvest_date', 'cost_price', 'Shelf_life',)

admin.site.register(product, productAdmin)
admin.site.register(make_order)

@admin.register(Sell_poultry)
class Sell_poultry_Admin(admin.ModelAdmin):
    list_display = ['product', 'caption', 'date_posted', 'price', 'picture',] 
    search_fields = ['product__name', 'product__category', 'product__shelf_life' 'caption']  
    list_filter = ['product'] 
    readonly_fields = ['date_posted'] 

@admin.register(Sell_cattle)
class Sell_cattle_Admin(admin.ModelAdmin):
    list_display = ['product', 'caption', 'date_posted', 'price', 'picture',] 
    search_fields = ['product__name', 'product__category', 'product__shelf_life' 'caption']  
    list_filter = ['product'] 
    readonly_fields = ['date_posted'] 


@admin.register(Sell_legumes)
class Sell_legumes_Admin(admin.ModelAdmin):
    list_display = ['product', 'caption', 'date_posted', 'price', 'picture',] 
    search_fields = ['product__name', 'product__category', 'product__shelf_life' 'caption']  
    list_filter = ['product'] 
    readonly_fields = ['date_posted'] 

@admin.register(Sell_roottubers)
class Sell_roottubers_Admin(admin.ModelAdmin):
    list_display = ['product', 'caption', 'date_posted', 'price', 'picture',] 
    search_fields = ['product__name', 'product__category', 'product__shelf_life' 'caption']  
    list_filter = ['product'] 
    readonly_fields = ['date_posted'] 

@admin.register(Sell_cereals)
class Sell_cereals_Admin(admin.ModelAdmin):
    list_display = ['product', 'caption', 'date_posted', 'price', 'picture',] 
    search_fields = ['product__name', 'product__category', 'product__shelf_life' 'caption']  
    list_filter = ['product'] 
    readonly_fields = ['date_posted'] 


