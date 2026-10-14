from datetime import datetime
import matplotlib.pyplot as plt

def generar_csv(filtrados, ruta_csv):
    columnas= ["fecha", "hora", "valor"]
    with open(ruta_csv, "w", encoding="utf-8") as archivo:
        archivo.write(",".join(columnas)+"\n")
        for dato in filtrados:
            fila = []
            for col in columnas:
                valor = dato[col]
                fila.append(str(valor))
            archivo.write(",".join(fila)+"\n") 

def generar_grafica(filtrados, estacion, medicion):
    lista_horas = []
    lista_valores = []
    for dato in filtrados:
        lista_horas.append(dato["hora"])
        lista_valores.append(dato["valor"])
    fecha = datetime.now().strftime("%Y-%m-%d")
    nombre_estacion = estacion.lower().replace(" ", "_")
    ruta_png = f"appweb/salidas/{fecha}_{nombre_estacion}_{medicion}.png"
    plt.plot(lista_horas, lista_valores)
    plt.title(estacion)
    plt.xlabel("Horas")
    plt.ylabel(medicion.capitalize())
    plt.savefig(ruta_png)
    plt.close()
    return ruta_png