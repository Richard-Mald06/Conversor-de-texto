# Trabajo Practico Integrador 1

## Descripcion 
Programa para procesar datos meteorologicos del Servicio Meteorologico Nacional y convertirlos posteriormente de TXT a JSON para ser visible a traves de una pagina web. 

## Grupo e Integrantes
Nombre: Peabody y Sherman 
Integrantes: Ricardo Maldonado y Daiana Parra 

## Forma de Ejecucion Prevista 
El programa recibe un archivo TXT como entrada, interpreta sus registros, realiza las validaciones correspondientes y separa los registros válidos de los inválidos.
Como resultado, se genera un archivo JSON que contiene la información del procesamiento, los registros válidos y los registros inválidos. Este archivo será utilizado posteriormente en una aplicacion de streamlit 

## Requirements
pip install -r requirements.txt

## Comandos para ejecutar en terminal
Todos los comandos se ejecutan desde la carpeta Conversor-de-texto (aclarado en la seccion de procesamiento)
# Etapa 1
- conversor txt a JSON: python conversor/adaptar_datos.py appweb/datos/mediciones.txt appweb/datos

- procesamiento: python appweb/procesar_datos.py <ruta_json> "<ESTACION>" <medicion> (la ruta del json incluye appweb/datos/ ya que se ejecuta desde el conversor de texto) por ejemplo: python appweb/procesar_datos.py appweb\datos\mediciones-20261012-151247.json "BASE BELGRANO II" humedad   

# Etapa 2
- streamlit run appweb/app.py -- appweb/datos/<nombre_json>.json por ejemplo: streamlit run appweb/app.py -- appweb/datos/mediciones-20261012-151247.json

## Salidas
Los archivos CSV y PNG generados se guardan en appweb/salidas/
La estructura de nombre que tienen es AAAA-MM-DD_estacion_medicion (ejemplo: 2026-10-16_aeroparque_aero_temperatura)


# Debilidades/Puntos a mejorar:
- Registros que tengan una medicion completa sin datos (por ejemplo la presión) se descarta entero, por eso estaciones como Bariloche no aparecen en la app.
- Se acepta cualquier fecha real, sin restricción de años