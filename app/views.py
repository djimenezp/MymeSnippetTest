from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app import models, serializers


class ListCreateRetrieveMixin(mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.ListModelMixin,
                              GenericViewSet):
    pass


class OrderViewSet(ListCreateRetrieveMixin):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class RestockViewSet(ListCreateRetrieveMixin):
    queryset = models.Restock.objects.all()
    serializer_class = serializers.RestockSerializer


class ProductViewSet(ListCreateRetrieveMixin):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class WarehouseViewSet(ListCreateRetrieveMixin):
    queryset = models.Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer
