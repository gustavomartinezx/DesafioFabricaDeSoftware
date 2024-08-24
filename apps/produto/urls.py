from django.urls import path, include

from rest_framework import routers

from apps.produto.api.viewset import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]