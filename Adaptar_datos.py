import json
lista = []
with open("2prueba.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
for numero, linea in enumerate(lineas):
    if numero < 2:
        continue
    linea = linea.strip()
    if linea == "":
        continue
    lista.append(linea)
for linea in lista:
    campos = linea.strip().split()
    print(campos)
