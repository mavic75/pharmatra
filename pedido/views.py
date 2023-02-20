from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Cargo, Cliente, Producto
from .serializers import CargoSerializer, ClienteSerializer, ProductoSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo")

def cargos(request):
    post_descripcion = request.POST.get('descripcion')
    if post_descripcion:
        q = Cargo(descripcion=post_descripcion)
        q.save()

    filtro_descripcion = request.GET.get('descripcion')
    if filtro_descripcion:
        cargos = Cargo.objects.filter(descripcion__contains=filtro_descripcion)
    else:
        cargos = Cargo.objects.all()
    return render(request, "form_cargos.html", {
        "cargos": cargos
    })

@api_view(["GET"])
def cargos_count(request):
    try:
        cantidad = Cargo.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)

def clientes(request):
    post_nombre = request.POST.get('nombre')
    post_ci = request.POST.get('ci')
    post_unidad = request.POST.get('unidad')
    post_direccion = request.POST.get('direccion')
    if post_nombre and post_ci and post_telefono and post_direccion:
        q = Cliente(nombre=post_nombre, ci=post_ci, telefono=post_telefono, direccion=post_direccion)
        q = save()
    
    filtro_nombre = request.GET.get('nombre')
    if filtro_nombre:
        clientes = Cliente.objects.filter(nombre__contains=filtro_nombre)
    else:
        clientes = Cliente.objects.all()
    return render(request, "form_clientes.html", {
        "clientes":clientes
    })

def productos(request):
    post_nombre = request.POST.get('nombre')
    post_descripcion = request.POST.get('descripcion')
    post_unidad = request.POST.get('unidad')
    post_precio = request.POST.get('precio')
    post_presentacion = request.POST.get('presentacion')
    post_laboratorio = request.POST.get('laboratorio')
    post_observacion = request.POST.get('observacion')
    if post_nombre and post_descripcion and post_unidad and post_precio and post_presentacion and post_laboratorio and post_observacion:
        q = Producto(nombre=post_nombre, descripcion=post_descripcion, unidad=post_unidad, precio=post_precio, presentacion=post_presentacion, laboratorio=post_laboratorio, observacion=post_observacion)
        q = save()
    
    filtro_nombre = request.GET.get('nombre')
    if filtro_nombre:
        productos = Producto.objects.filter(nombre__contains=filtro_nombre)
    else:
        productos = Producto.objects.all()
    return render(request, "form_productos.html", {
        "productos":productos
    })

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer