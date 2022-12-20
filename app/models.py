from django.db import models


class Warehouse(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField(default=0)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        return super(Warehouse, self).save(force_insert, force_update, using, update_fields)

    def current_inventory(self):
        return sum([i.stock or 0 for i in self.products.all()])


class Product(models.Model):
    sku = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    ean = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(null=True)
    warehouse = models.ForeignKey("Warehouse", models.CASCADE, 'products')

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)


class Order(models.Model):
    status = models.CharField(max_length=200)


class OrderLine(models.Model):
    order = models.ForeignKey("Order", models.CASCADE, related_name='order_lines')
    product = models.ForeignKey("Product", models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.product.stock = self.product.stock or 0
        self.product.stock -= self.quantity
        self.product.save()
        return super().save(force_insert, force_update, using, update_fields)


class Restock(models.Model):
    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        return super().save(force_insert, force_update, using, update_fields)


class RestockLine(models.Model):
    restock = models.ForeignKey("Restock", models.CASCADE, 'restock_lines')
    product = models.ForeignKey("Product", models.CASCADE)
    quantity = models.PositiveIntegerField()

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.product.stock = self.product.stock or 0
        self.product.stock += self.quantity
        self.product.save()
        super().save(force_insert, force_update, using, update_fields)
