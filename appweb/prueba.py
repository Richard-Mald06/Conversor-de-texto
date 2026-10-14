from datos import cargar_json, filtrar_datos
from graficos import generar_csv

datos = cargar_json("appweb/datos/mediciones-20261012-151247.json")
filtrados = filtrar_datos(datos, "BAHIA BLANCA AERO", "temperatura")
generar_csv(filtrados, "appweb/salidas/prueba_bahia_temperatura.csv")
print("CSV generado")