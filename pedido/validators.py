from django.core.exceptions import ValidationError

def validar_preciopositivo(value):
    if value < 0:
        raise ValidationError(
            '%(value)s no es un numero positivo',
            params={'value': value},
        )

def validar_precio_entrega(value):
    if value < 0:
        raise ValidationError(
            '%(values)s no es un numero positivo',
            params={'value': value},
        )