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

def validate_dir(value):
    a=value
    string=a.split()
    nom=False
    num=False
    for s in string:
        if s.isdigit():
            num=True
        else:
            nom=True
    if nom == False:
        raise ValidationError("La direccion no pueden ser solo numeros.")
    elif num == False:
        raise ValidationError("La direccion no tiene altura.")


def validate_pos(value):
    a=int(value)
    if a <0:
        raise ValidationError("El número no puede ser negativo.")

def validate_date(value):
    a=value
    dia=False
    mes=False
    año=False
    if a.day<32 and a.day>0:
        dia=True
    if a.month<13 and a.month>0:
        mes=True
    if a.year>0:
        año=True

    if dia == False:
        raise ValidationError("El dia no es valido.")
    if mes == False:
        raise ValidationError("El mes no es valido.")
    if año == False:
        raise ValidationError("El año no es valido.")
