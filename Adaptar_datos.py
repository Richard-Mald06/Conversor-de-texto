import json
import sys
import validaciones
#python adaptar_datos.py datos/mediciones.txt datos/observaciones.json
archivo_medicion = sys.argv[1]
observaciones = sys.argv[2]

lista = []
with open(archivo_medicion, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
for numero, linea in enumerate(lineas):
    if numero < 2:
        continue
    linea = linea.strip()
    if linea == "":
        continue
    lista.append(linea)

diccionario_datos = {"resumen":{"total_registros" : 0,
                                "registros_validos" : 0,
                                "registros_invalidos" : 0                                
                                },
                     "datos_validos":[],
                     "datos_invalidos":[],
}

diccionario_motivos = {
    "parametros" : "faltan datos numericos",
    "fecha" : "formato de fecha no valido",
    "hora" : "hora no valida",
    "temperatura" : "temperatura no valida/fuera de rango",
    "humedad" : "humedad no valida/fuera de rango",
    "presion" : "presion no valida/fuera de rango",
    "direccion" : "direccion no valida",
    "velocidad" : "velocidad no valida/fuera de rango",
    "nombre" : "formato de nombre no valido",
}

for linea in lista:
    campos = linea.strip().split()
    
    if validaciones.cant_datos_numericos(campos) != 7:
        diccionario_datos["datos_invalidos"].append({
            "linea": linea, 
            "motivo": diccionario_motivos["parametros"]
        })
        continue

    if not validaciones.validar_fecha(campos[0]):
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["fecha"]
            })
        continue

    if not validaciones.validar_hora(campos[1]):
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["hora"]
        })
        continue

    if not validaciones.validar_temp(campos[2]):
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["temperatura"]
        })
        continue

    if not validaciones.validar_humedad(campos[3]):
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["humedad"]
        })
        continue

    if not validaciones.validar_presion(campos[4]):
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["presion"]
        })
        continue

    if not validaciones.validar_direccion(campos[5]):
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["direccion"]
        })
        continue

    if not validaciones.validar_velocidad(campos[6]):
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["velocidad"]
        })
        continue

    nombre_estacion = " ".join(campos[7:])
    if not validaciones.validar_estacion(nombre_estacion):
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["nombre"]
        })
        continue

    fecha_valida = int(campos[0])
    hora_valida = int(campos[1])
    temperatura_valida = float(campos[2])
    humedad_valida = int(campos[3])
    presion_valida = float(campos[4])
    direccion_valida = int(campos[5])
    velocidad_valida = int(campos[6])
    estacion_valida = str(nombre_estacion)

    diccionario_datos["datos_validos"].append({
        "fecha" : fecha_valida,
        "hora" : hora_valida,
        "temperatura" : temperatura_valida,
        "humedad" : humedad_valida,
        "presion" : presion_valida,
        "direccion" : direccion_valida,
        "velocidad" : velocidad_valida,
        "estacion" : estacion_valida
    })

cant_registros = len(diccionario_datos["datos_validos"]) + len(diccionario_datos["datos_invalidos"])
cant_validos = len(diccionario_datos["datos_validos"])
cant_invalidos = len(diccionario_datos["datos_invalidos"])

diccionario_datos["resumen"]["total_registros"] = cant_registros
diccionario_datos["resumen"]["registros_validos"] = cant_validos
diccionario_datos["resumen"]["registros_invalidos"]= cant_invalidos

print(f"----------resumen----------")
print(f"la cantidad de registros leidos fue {cant_registros}")
print(f"registros validos: {cant_validos}")
print(f"registros invalidos: {cant_invalidos}")

with open(observaciones, "w", encoding="utf-8") as datos_salida:
    json.dump(diccionario_datos, datos_salida, indent=2)