from django.contrib import admin

from interview.order.models import OrderTag, Order


# Register your models here.
@admin.register(OrderTag)
class OrderTagAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ["inventory__type", "start_date"]
    list_display = ["inventory", "start_date", "embargo_date"]
    list_filter = ["inventory", "start_date", "embargo_date"]
