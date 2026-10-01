import json
import sys
import validaciones
print(sys.argv[1])

#python adaptar_datos.py datos/mediciones.txt datos/observaciones.json
archivo_medicion = sys.argv[1]
observaciones = sys.argv[2]
print(observaciones)

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


diccionario_datos = {"datos_validos":[],
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

i= 0
for linea in lista:
    i +=1
    campos = linea.strip().split()
    
    if validaciones.cant_datos_numericos(campos) != 7:
        print(f"linea invalida {linea}, faltan datos")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea, 
            "motivo": diccionario_motivos["parametros"]
        })
        continue
    else:
        print(f"la linea: {linea} posee  una cantidad de parametros valida ")

    if validaciones.validar_fecha(campos[0]):
        print(f"la linea: {linea} tiene una fecha valida")
    else:
        print(f"linea invalida {linea} el formato de fecha no es el adecuado")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["fecha"]
            })
        continue

    if validaciones.validar_hora(campos[1]):
        print(f"la linea: {linea} tiene una hora valida")
    else:
        print(f"linea invalida: {linea}, formato de hora no valido ")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["hora"]
        })
        continue

    if validaciones.validar_temp(campos[2]):
        print(f"la linea:{linea} tiene una temperatura valida")
    else:
        print(f"linea invalida {campos[2]} no es una temperatura valida")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["temperatura"]
        })
        continue

    if validaciones.validar_humedad(campos[3]):
        print(f"la linea:{linea} tiene una humedad valida") 
    else:
        print(f"linea invalida {campos[3]} no es una humedad valida")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["humedad"]
        })
        continue

    if validaciones.validar_presion(campos[4]):
        print(f"la linea:{linea} tiene una presion valida") 
    else:
        print(f"linea invalida {campos[4]} no es una presion valida")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["presion"]
        })
        continue

    if validaciones.validar_direccion(campos[5]):
        print(f"la linea:{linea} tiene una direccion valida") 
    else:
        print(f"linea invalida {campos[5]} no es una direccion valida")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["direccion"]
        })
        continue

    if validaciones.validar_velocidad(campos[6]):
        print(f"la linea:{linea} tiene una velocidad valida") 
    else:
        print(f"linea invalida {campos[6]} no es una velocidad valida")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["velocidad"]
        })
        continue

    nombre_estacion = " ".join(campos[7:])
    print(nombre_estacion)
    if validaciones.validar_estacion(nombre_estacion):
        print(f"la linea:{linea} tiene una estacion valida") 
    else:
        print(f"linea invalida {nombre_estacion} no es una estacion valida")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["nombre"]
        })
        continue

    print(f"verificacion {i}---------------")

    fecha_valida = int(campos[0])
    hora_valida = int(campos[1])

    diccionario_datos["datos_validos"].append({
        "fecha" : fecha_valida
    })
    

with open(observaciones, "w", encoding="utf-8") as datos_salida:
    json.dump(diccionario_datos, datos_salida, indent=2)