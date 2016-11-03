from django.contrib import admin
from models import *


# Register your models here.
class ProductInfoInline(admin.TabularInline):
    model = ProductInfo
    extra = 1


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'uName', 'uPwd', 'uEmail', 'uPhone', 'uAddr', 'uTime']


class CartListAdmin(admin.ModelAdmin):
    list_display = ['id', 'cPrice', 'cNum', 'cUser', 'cProduct']


class OrderListAdmin(admin.ModelAdmin):
    list_display = ['id', 'oUser', 'oSum', 'oIspay', 'oTime']


class DetailOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'dProduct', 'dNum', 'dPrice', 'dMain']


class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pName', 'pPrice', 'pStock',
                    'pDesc', 'pDetail', 'pTime', 'pClass']


class SortAdmin(admin.ModelAdmin):
    list_display = ['id', 'sClass']
    inlines = [ProductInfoInline]


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(CartList, CartListAdmin)
admin.site.register(OrderList, OrderListAdmin)
admin.site.register(DetailOrder, DetailOrderAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
admin.site.register(Sort, SortAdmin)
