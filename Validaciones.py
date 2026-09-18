def validar_cant_parametros(parametros):
    if len(parametros)>=8:
        return True
    else:
        return False

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
    if -30 < temperatura < 50:
        return True
    return False
