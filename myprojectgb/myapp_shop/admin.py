from django.contrib import admin
from .models import ProductNew, Order, User


@admin.action(description='обнулить количество')
def reset_quant(modeladmin, request, queryset):
    queryset.update(count=0)


class NewProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    list_filter = ['price']
    search_fields = ['name']
    actions = [reset_quant]


class ItemInline(admin.StackedInline):
    model = Order
    extra = 0


class NewUserAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ['name', 'phone_number', 'date_reg']
    search_fields = ['name']


class NewOrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order_sum', 'order_date']
    list_filter = ['order_sum', 'order_date']
    ordering = ['order_date', '-order_sum']


admin.site.register(ProductNew, NewProductAdmin)
admin.site.register(Order, NewOrderAdmin)
admin.site.register(User, NewUserAdmin)
