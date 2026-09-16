def validar_cant_parametros(parametros):
    if len(parametros)>=8:
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

def validar_fecha(fecha):
    dia = fecha[0:2]
    mes = fecha[2:4]
    año = fecha[4:8]