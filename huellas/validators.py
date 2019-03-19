from django.core.exceptions import ValidationError

def validate_dni(value):
    count = 0
    for c in str(value):
        count += 1
    if count <8:
            raise ValidationError("El numero es muy corto para ser un DNI.")
    return value

def validate_cel(value):
    count = 0
    for c in str(value):
        count += 1
    if count <8:
            raise ValidationError("El numero es muy corto para ser un celular.")
    return value

def validate_tel(value):
    count = 0
    for c in str(value):
        count += 1
    if count <6:
            raise ValidationError("El numero es muy corto para ser numero de telefono.")
    return value

def validate_str(value):
    string=value
    if string.isdigit():
        raise ValidationError("El campo ingresado no puede contener numeros.")
    return value