def cant_datos_numericos(campos):
    i = 0
    for elemento in campos:
        try:
            float(elemento)
            i += 1
        except ValueError:
            return i
    return i

def validar_fecha(fecha):
    if len(fecha) != 8:
            return False
    try:
        dia = int(fecha[0:2])
        mes = int(fecha[2:4])
        anio = int(fecha[4:])
    except ValueError:
        return False
    if 1<= dia <= 31 and 1<= mes <= 12 and 2000 <= anio <= 2030:
            return True
    else:
        return False

def validar_hora(hora):
    if len(hora) > 2:
        return False
    try:
        hora = int(hora)
    except ValueError:
        return False
    if 0 <= hora <= 23:
        return True
    else:
        return False

def validar_temp(temperatura):
    try:
        temperatura = float(temperatura)
    except ValueError:
        return False
    if -35 <= temperatura <= 50:
        return True
    return False

def validar_humedad(humedad):
    try:
        humedad = int(humedad)
    except ValueError:
        return False
    if 0 < humedad <= 100:
        return True
    return False

def validar_presion(presion):
    try:
        presion = float(presion)
    except ValueError:
        return False
    if 960 <= presion <= 1060:
        return True
    return False

def validar_direccion(direccion):
    try:
        direccion = int(direccion)
    except ValueError:
        return False
    if 0 <= direccion <= 360:
        return True
    return False

def validar_velocidad(velocidad):
    try:
        velocidad = int(velocidad)
    except ValueError:
        return False
    if 0 <= velocidad <= 150:
        return True
    return False

def validar_estacion(nombre):
    nombre = str(nombre).strip()
    if nombre:
        return True
    return False