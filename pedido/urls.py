from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"cargos", views.CargoViewSet)
router.register(r"clientes", views.ClienteViewSet)
router.register(r"productos", views.ProductoViewSet)

urlpatterns = [
    # path("", views.index, name="index")
    path("cargos", views.cargos, name="cargos"),
    path("cargos/cantidad/", views.cargos_count, name="contador"),
    path("clientes", views.clientes, name="clientes"),
    path("productos", views.productos, name="productos"),
    path("", include(router.urls)),
]