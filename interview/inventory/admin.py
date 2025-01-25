from django.contrib import admin

from interview.inventory.models import InventoryTag, InventoryLanguage, InventoryType, Inventory


# Register your models here.
@admin.register(InventoryTag)
class InventoryTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(InventoryLanguage)
class InventoryLanguageAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(InventoryType)
class InventoryTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("type", "language", "tags")
    list_display = ("name", "type", "language")
    list_select_related = ("type", "language")
    filter_horizontal = ("tags",)
    readonly_fields = ("metadata",)
