from django.contrib import admin

from app import models


class Default(admin.ModelAdmin):
    pass


@admin.register(models.Warehouse)
class WarehouseAdmin(Default):
    list_display = ['location', 'current_inventory']
    readonly_fields = ('current_inventory',)


@admin.register(models.Product)
class ProductAdmin(Default):
    list_display = ['sku', 'name', 'ean', 'warehouse', 'stock']
    readonly_fields = ('stock',)
    pass


@admin.register(models.OrderLine)
class OrderLineAdmin(Default):
    pass


class OrderLineInline(admin.TabularInline):
    model = models.OrderLine


@admin.register(models.Order)
class OrderAdmin(Default):
    inlines = [
        OrderLineInline,
    ]


@admin.register(models.RestockLine)
class RestockLineAdmin(Default):
    pass


class RestockLineInline(admin.TabularInline):
    model = models.RestockLine


@admin.register(models.Restock)
class RestockAdmin(Default):
    inlines = [
        RestockLineInline,
    ]
