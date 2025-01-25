from django.contrib import admin

from interview.order.models import Order, OrderTag


# Register your models here.
@admin.register(OrderTag)
class OrderTagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'is_active', 'created_at', 'updated_at')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('inventory__type', 'start_date', 'embargo_date')
    list_display = ('inventory', 'start_date', 'embargo_date', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'tags')
    filter_horizontal = ('tags',)
