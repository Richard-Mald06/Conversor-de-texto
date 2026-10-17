import sys
import json
import pandas as pd
import streamlit as st
from datos import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica, generar_csv
from datetime import datetime

# streamlit run app.py -- datos/observaciones.json
# comando REAL streamlit run appweb/app.py -- appweb/datos/observaciones.json
print(sys.argv)

if len(sys.argv) != 2:
    st.error("cantidad de argumentos en terminal no valida")
    st.stop()

st.title("Aplicacion Lectura de Datos")

ruta_json = sys.argv[1]


try:
    datos = cargar_json(ruta_json)
except FileNotFoundError:
    st.error("no se encontro el archivo")
    st.stop()
except json.decoder.JSONDecodeError:
    st.error("el archivo existe pero no es un json valido")
    st.stop()


estaciones = set()
mediciones = ["temperatura", "humedad", "presion", "direccion", "velocidad"]

for dato in datos["datos_validos"]:
    estacion = dato["estacion"]
    estaciones.add(estacion)

estacion = st.selectbox("Ingrese la estacion: ", sorted(list(estaciones)))
medicion = st.selectbox("Ingrese la medicion: ", mediciones)

filtrados_var = filtrar_datos(datos, estacion, medicion)
if not filtrados_var:
    st.error("no hay datos filtrados")
    st.stop()


estadisticas_calc = calcular_estadisticas(filtrados_var)
ruta_grafica = generar_grafica(filtrados_var, estacion, medicion)

fecha_csv = datetime.now().strftime("%Y-%m-%d")
nombre_estacion = estacion.lower().replace(" ", "_")
ruta_csv = f"appweb/salidas/{fecha_csv}_{nombre_estacion}_{medicion}.csv"
#mediciones = pd.read_csv("appweb/salidas/2026-10-14_bahia_blanca_aero_temperatura.csv")

filtrados_dataframe = pd.DataFrame(filtrados_var)

st.header("Diccionario de las estadisticas")
st.write(estadisticas_calc)

st.header("Tabla de datos filtrados")
st.markdown("**Aviso: La tabla muestra solo los datos que fueron tomados como validos**")
st.dataframe(filtrados_dataframe)

st.header("Grafico de función")
st.markdown("**Aviso: La grafica muestra solo los datos que fueron tomados como validos**")
st.image(ruta_grafica, caption=f"Grafico: comportamiento de {medicion} en funcion del tiempo")


if st.button("Generar del CSV"):
    generar_csv(filtrados_var, ruta_csv)
    st.success(f"la ruta del CSV generado es: {ruta_csv}")