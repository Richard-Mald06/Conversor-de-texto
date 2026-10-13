def calcular_estadisticas(filtrados):
    cantidad = len(filtrados)
    suma = 0
    minimo = filtrados[0]["valor"]
    maximo = filtrados[0]["valor"]
    for dato in filtrados:
        if dato["valor"] < minimo:
            minimo = dato["valor"]
        if dato["valor"] > maximo:
            maximo = dato["valor"]
        suma += dato["valor"]
    promedio = suma/cantidad
    return {
        "cantidad": cantidad,
        "minimo": minimo,
        "maximo": maximo,
        "promedio": promedio
    }