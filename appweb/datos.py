import json
def cargar_json(ruta_json):
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return datos

def filtrar_datos(datos, estacion, medicion):
    filtrados = []
    for dato in datos["datos_validos"]:
        if estacion.upper() == dato["estacion"].upper():
            filtrados.append({
                "fecha": dato["fecha"],
                "hora": dato["hora"],
                "valor": dato[medicion]
                })        
    return filtrados