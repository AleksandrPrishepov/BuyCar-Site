from django.contrib import admin
from car.models import *

class AutoBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'slug_brand', 'sign_auto')
    list_display_links = ('brand',)
    search_fields = ('brand',)
    list_filter = ('brand',)
    prepopulated_fields = {"slug_brand": ("brand",)}

class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'slug_model')
    list_display_links = ('model',)
    search_fields = ('model',)
    list_filter = ('model',)
    prepopulated_fields = {"slug_model": ("model",)}

class OwnerAutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_owner', 'brand_owner',
                    'model_owner', 'photo', 'year_old',
                    'slug_owner', 'time_create', 'time_update',
                    'is_published', 'cat_car_brand')
    list_display_links = ('name_owner', 'brand_owner')
    search_fields = ('brand_owner', 'model_owner')
    list_editable = ('is_published',)
    list_filter = ('brand_owner', 'time_create', 'model_owner', 'year_old')
    prepopulated_fields = {'slug_owner': ('name_owner',)}

admin.site.register(AutoBrand, AutoBrandAdmin)
admin.site.register(AutoModel, AutoModelAdmin)
admin.site.register(OwnerAuto, OwnerAutoAdmin)