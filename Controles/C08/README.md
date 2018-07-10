# Control 8

### Verdadero o falso (2 ptos)

1. Serializar un objeto en Python con `pickle` permite deserializar el archivo binario en cualquier programa escrito en Python.

	* Verdadero (0.4 pts)

2. La serialización y deserialización en JSON, sin ninguna personalización, permite almacenar y recuperar cualquier tipo de dato de los que vienen por defecto con Python.

	* Verdadero (0.4 pts)

3. Respecto a la comunicación de dos procesos en red, los puertos por los que se recibe información en el cliente y el servidor tienen que ser los mismos.

	* Falso, cada uno puede tener el socket de la comunicación asociado a un puerto distinto.  (0.8 pts)

4. En el protocolo de transporte UDP no se necesita establecer una conexión para enviar los datos.

	* Verdadero  (0.4 pts)

### Desarrollo rápido (2 ptos)

1. En un modelo cliente-servidor, ¿quién inicia la comunicación? ¿Quién escucha?

	* El cliente inicia la comunicación y el servidor escucha. (0.6 pts)

2. Suponga que quiere construir un cliente de mensajería para competir contra Whatsapp.
	* **a)** Para los usuarios es fundamental que los mensajes lleguen a destino, o en el peor caso, saber que un mensaje no llegó. A raíz de esto, ¿qué protocolo de transporte usaría en su programa?
	* TCP porque asegura fiabilidad (0.4 pts)
	* **b)** El profesor de la otra sección le sugiere que sea el servidor donde se implemente el *back-end* de la aplicación. ¿Tiene razón? Justifique su respuesta.
	* Sí, porque así se maneja el modelo de datos y validaciones sin que los clientes se involucren directamente y se hace de forma centralizada. (1 pt)

### Escritura de código (2 ptos)

Suponga que tiene el siguiente código en Python.

```
import json

class Partido:
	def __init__(self, ubicacion, local, visita, resultado):
		self.ubicacion = ubicacion
		self.local = local
		self.visita = visita
		self.resultado = resultado
```  

Y que, además, tiene un archivo llamado `objetos.json` con el siguiente contendio:

```
[
{"ubicacion": "Moscú", "local": "Rusia", "visita": "Arabia Saudita", "resultado": "5-0"},
{"ubicacion": "Moscú", "local": "Argentina", "visita": "Islandia", "resultado": "1-1"},
{"ubicacion": "Rostov-on-Don", "local": "Brasil", "visita": "Suiza", "resultado": "1-1"},
{"ubicacion": "Saransk", "local": "Colombia", "visita": "Japón", "resultado": "1-2"},
{"ubicacion": "Saransk", "local": "Perú", "visita": "Dinamarca", "resultado": "0-1"}
]
```

Implemente la función `get_partido(filepath='objetos.json')` en Python. Esta debe recibir un *filepath* en forma de *string*, y retornar una lista de objetos de tipo `Partido`, a partir del contenido del archivo.

**Solución propuesta**

```
def get_partidos(filepath='objetos.json'):
	with open(filepath, 'r', encoding='utf-8') as file:
		data = json.load(file, object_hook=lambda dic: Partido(**dic))
	return data

```

Distribución de puntaje:

* 0.5 pts por leer el archivo
* 0.5 pts por usar load con `object_hook`
* 1 pt por pasarle como `object_hook` una función que toma un diccionario y entrega un objeto `Partido`.
