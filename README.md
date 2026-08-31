# Trabajo Practico Integrador 1

## Descripcion 
Programa para procesar datos meteorologicos del Servicio Meteorologico Nacional y convertirlos posteriormente de TXT a JSON para ser visible a
traves de una pagina web. 

## Grupo e Integrantes
Nombre: Peabody y Sherman 
Integrantes: Ricardo Maldonado y Daiana Parra 

## Instalacion 
python 

## Comandos de Ejecucion Prevista 
El programa se ejecutara desde la terminal mediante el siguiente comando: 
python adaptar_datos.py datos/mediciones.txt datos/mediciones.json

- adaptar_datos.py : Programa Principal (lugar donde se procesan los datos)
- mediciones.txt : Entrada del archivo TXT 
- mediciones.json : Salida de los datos convertidos a archivo JSON

## Explicacion 
TXT -> leer archivo -> recorrer líneas -> ignorar encabezados/líneas vacías -> separar campos -> validar -> válido / inválido -> JSON

## Documentacion del Formato JSON Generado 
La forma en la que pensamos que se implemente el JSON a la salida es a traves de clave-valor. 
