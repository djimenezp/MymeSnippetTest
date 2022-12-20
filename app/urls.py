from django.urls import path, include
from rest_framework import routers

from app import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'order', views.OrderViewSet)
router.register(r'restock', views.RestockViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'warehouse', views.WarehouseViewSet)

urlpatterns = [
    # path('', views.APIRoot.as_view()),
    path('/', include(router.urls))
]
