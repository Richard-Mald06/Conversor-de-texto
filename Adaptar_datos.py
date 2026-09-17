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

for linea in lista:
    campos = linea.strip().split()
    
    if validaciones.validar_cant_parametros(campos):
        print(f"la linea {linea} posee una cantidad de parametros valida")
        # print(campos)
        # print(campos[0])
        # diccionario_datos["datos_validos"].append(linea)      
    else:
        motivo = "cantidad de parametros insuficiente"
        print(f"linea invalida {linea} no tiene la cantidad de parametros necesaria")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": motivo
        })
    # print(campos)
    if validaciones.validar_fecha(campos[0]):
        print(f"la linea {linea} tiene una fecha valida")
    else:
        motivo  = "formato de fecha invalido"
        print(f"linea invalida {linea} el formato de fecha no es el adecuado")
        diccionario_datos["datos_invalidos"].append({
            "linea": linea,
            "motivo": motivo
            })
    print("---------------")


with open(observaciones, "w", encoding="utf-8") as datos_salida:
    json.dump(diccionario_datos, datos_salida, indent=2)