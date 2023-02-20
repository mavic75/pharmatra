from django import forms
from .models import Cargos, Cliente, Producto


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"