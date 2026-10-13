import json
def cargar_json(ruta_json):
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return datos

def filtrar_datos(datos, estacion, medicion):
    lista_datos = []
    for dato in datos["datos_validos"]:
        if estacion.upper() == dato["estacion"].upper():
            lista_datos.append({
                "fecha": dato["fecha"],
                "hora": dato["hora"],
                "valor": dato[medicion]
                })        
    return lista_datos