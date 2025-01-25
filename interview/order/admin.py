from django.contrib import admin

from interview.order.models import OrderTag, Order


# Register your models here.
@admin.register(OrderTag)
class OrderTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
