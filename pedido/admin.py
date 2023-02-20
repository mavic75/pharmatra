from django.contrib import admin

from .models import Producto, Pedido, Cargo,Cliente, DetalleCargo

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Cargo)
admin.site.register(Cliente)
admin.site.register(DetalleCargo)