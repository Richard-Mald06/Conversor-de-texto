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
        
        print(campos)
        print(campos[0])
        diccionario_datos["datos_validos"].append(linea)
    else:
        print(f"linea invalida {linea}")
        diccionario_datos["datos_invalidos"].append(linea)

    # print(campos)




with open(observaciones, "w", encoding="utf-8") as datos_salida:
    json.dump(lista, datos_salida, indent=2)