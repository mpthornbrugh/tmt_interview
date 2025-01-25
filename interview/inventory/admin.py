from django.contrib import admin

from interview.inventory.models import InventoryTag, InventoryLanguage, InventoryType, Inventory


# Register your models here.
@admin.register(InventoryTag)
class InventoryTagAdmin(admin.ModelAdmin):
    pass


@admin.register(InventoryLanguage)
class InventoryLanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(InventoryType)
class InventoryTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass
