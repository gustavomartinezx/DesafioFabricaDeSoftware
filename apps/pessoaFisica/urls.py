from django.urls import path, include

from rest_framework import routers

from apps.pessoaFisica.api.viewset import ClienteViewSet, FuncionarioViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet,)
router.register(r'funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
