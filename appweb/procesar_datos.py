from datetime import datetime
import sys
import json
from datos import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica, generar_csv



mediciones_validas = ["temperatura", "humedad", "presion", "direccion", "velocidad"]
def main():

    if len(sys.argv) != 4:
        print("cantidad de argumentos no valida")
        sys.exit(1)

    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    if medicion not in mediciones_validas:
        print("Esa medicion no es parte del programa")
        sys.exit(1)
        
    try:
        datos = cargar_json(ruta_json)
    except FileNotFoundError:
        print("La ruta del archivo no existe o es incorrecta")
        sys.exit(1)
    except json.decoder.JSONDecodeError:
        print("el archivo existe pero no es un json valido")
        sys.exit(1)

    filtrados = filtrar_datos(datos, estacion, medicion)
    if not filtrados:
        print("no hay datos filtrados")
        sys.exit(1)

    estadisticas = calcular_estadisticas(filtrados)

    #para generar el csv
    fecha_csv = datetime.now().strftime("%Y-%m-%d")
    nombre_estacion = estacion.lower().replace(" ", "_")
    ruta_csv = f"appweb/salidas/{fecha_csv}_{nombre_estacion}_{medicion}.csv"
    generar_csv(filtrados, ruta_csv)

    ruta_grafica = generar_grafica(filtrados, estacion, medicion)

    print(estadisticas)
    print("los primeros registros filtrados son: ")
    for filtrado in filtrados[:3]:
        print(filtrado)

    print(f"Grafica guardada en: {ruta_grafica}")
    print(f"archivo csv guardado en: {ruta_csv}")


main()