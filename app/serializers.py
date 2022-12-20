from rest_framework import serializers

from app import models


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = ('id', 'location', 'capacity', 'current_inventory')
        read_only_fields = ('id', 'current_inventory',)

    def validate(self, attrs):
        return attrs


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('name', 'sku', 'ean', 'stock', 'warehouse')
        read_only_fields = ('stock',)


class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderLine
        fields = ('id', 'product', 'quantity')
        read_only_fields = ('id', 'order',)

    def validate(self, attrs):
        if attrs['product'].stock - attrs['quantity'] < 0:
            raise serializers.ValidationError("No stock")
        return attrs


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_lines = OrderLineSerializer(many=True)

    class Meta:
        model = models.Order
        fields = ('id', 'url', 'status', 'order_lines')
        read_only_fields = ('id',)

    def create(self, validated_data):
        lines_data = validated_data.pop('order_lines')
        order = models.Order.objects.create(**validated_data)
        for line_data in lines_data:
            models.OrderLine.objects.create(order=order, **line_data)
        return order


class RestockLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RestockLine
        fields = ('id', 'product', 'quantity')
        read_only_fields = ('id', 'order',)

    def validate(self, attrs):
        warehouse = attrs['product'].warehouse
        if warehouse.current_inventory() + attrs['quantity'] > warehouse.capacity:
            raise serializers.ValidationError("Warehouse full")
        return attrs

    def create(self, validated_data):
        return super().create(validated_data)


class RestockSerializer(serializers.HyperlinkedModelSerializer):
    restock_lines = RestockLineSerializer(many=True)

    class Meta:
        model = models.Restock
        fields = ('id', 'url', 'restock_lines')
        read_only_fields = ('id',)

    def create(self, validated_data):
        lines_data = validated_data.pop('restock_lines')
        restock = self.Meta.model.objects.create(**validated_data)
        for line_data in lines_data:
            models.RestockLine.objects.create(restock=restock, **line_data)
        return restock
