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
    "parametros" : "cantidad de parametros no valida",
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
    campos = linea.strip().split()
    
    if not validaciones.validar_cant_parametros(campos): 
        print(f"linea invalida {linea} no tiene la cantidad de parametros necesaria")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["parametros"]
        })
        continue
    else:
        print(f"la linea: {linea} posee una cantidad de parametros valida")

    if validaciones.validar_fecha(campos[0]):
        print(f"la linea: {linea} tiene una fecha valida")
    else:
        print(f"linea invalida {linea} el formato de fecha no es el adecuado")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["fecha"]
            })
    if validaciones.validar_hora(campos[1]):
        print(f"la linea {linea} tiene una hora valida")
    else:
        print(f"linea invalida: {linea}, formato de hora no valido ")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["hora"]
        }
        )
    if validaciones.validar_temp(campos[2]):
        print(f"la linea:{linea} tiene una temperatura valida")
    else:
        print(f"linea invalida {campos[2]} no es una temperatura valida")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": diccionario_motivos["temperatura"]
        })
        
    print(f"verificacion {i}---------------")
    i +=1


with open(observaciones, "w", encoding="utf-8") as datos_salida:
    json.dump(diccionario_datos, datos_salida, indent=2)