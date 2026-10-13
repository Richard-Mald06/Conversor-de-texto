from datos import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas

datos = cargar_json("appweb/datos/mediciones-20261012-151247.json")
filtrados = filtrar_datos(datos, "BAHIA BLANCA AERO", "temperatura")
print(calcular_estadisticas(filtrados))

# Control manual con valores conocidos
print(calcular_estadisticas([{"valor": -2}, {"valor": 4}, {"valor": 1}]))