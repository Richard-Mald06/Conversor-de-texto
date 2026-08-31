Nombre del grupo: Peabody y Sherman 
Integrantes: Ricardo Maldonado y Daiana Parra 
Info de proyecto: Se va a divir el promraga en dos funciones: 
                1. Porgrama Principal: El programa principal cuenta con dos partes. La primera es donde recibe los datos validos y los convierte en un archivo JSON y despues donde lleva ese Archivo JSON a la pagina web. Pregunta: Los datos invalidos y leidos tambien se hacen archivo JSON con el fin de pasarlo a la pagina web? 
                2. Modulo de Validaciones: Trabaja antes del programa principal
Forma de ejecucion prevista: 
            Recibe un archivo txt de la red meteorologica argentina -> La informacion pasa por el modulo de validaciones -> Almacena en tres tipos de datos los numeros recibidos (valido, invalido y leido (todos los numeros)) -> Usa los datos validos y los lleva al programa -> En el programa se empieza a trabajar con los datos para hacerlo un archivo JSON -> El archivop JSON pasa a la pagina web -> Al final de la pagina web tambien se hace un resumen de todos los datos que entraron(los leidos), los datos validos y los invalidos 

La forma en la que pensamos que se implemente el JSON a la salida es a traves de clave-valor. 

Implementación inicial del parseo del TXT recibido por argumento de línea de comandos: 
