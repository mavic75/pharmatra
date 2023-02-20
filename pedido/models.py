from django.db import models
from .validators import validar_preciopositivo, validar_precio_entrega

# Create your models here.
class UserRoles(models.TextChoices):
    ADMINISTRADOR = 'adm', 'Adminstrador',
    VENDEDOR = 'ven', 'Vendedor',
    RECEPCION = 'rec', 'Recepcionista',

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    ci = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    rol = models.CharField(
        max_length = 3,
        choices = UserRoles.choices,
        default = UserRoles.VENDEDOR
    )
    status = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}"

class Cargo(models.Model):
    descripcion = models.CharField(max_length=30)
    usuarios = models.ManyToManyField(Usuario, through='DetalleCargo', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.descripcion}"

class DetalleCargo(models.Model):
    fecha_inicio = models.DateField()
    fecha_baja = models.DateField()
    status = models.BooleanField(blank=True, default=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=70)
    ci = models.CharField(max_length=15)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    unidad = models.CharField(max_length=15)
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio", validators=[validar_preciopositivo,])
    presentacion = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    observacion = models.TextField()
    status = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
class Pedido(models.Model):
    fecha = models.DateField()
    precio_entrega = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio de entrega", validators=[validar_precio_entrega,])
    monto_total = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Monto total")
    forma_pago = models.CharField(max_length=20)
    tipo_entrega = models.CharField(max_length=20)
    productos = models.ManyToManyField(Producto, through='DetallePedido', blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class DetallePedido(models.Model):
    cantidad = models.DateField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Delivery(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    observacion = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)