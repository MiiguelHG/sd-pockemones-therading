# PokeAPI.py

Este script de Python utiliza la [PokeAPI](https://pokeapi.co/) para obtener información sobre los primeros 100 Pokémon y mostrarla en la consola.  Utiliza hilos para realizar múltiples solicitudes a la API concurrentemente, lo que acelera el proceso de recuperación de datos.

## Funcionalidades

* Obtiene datos de los primeros 100 Pokémon.
* Utiliza hilos para realizar solicitudes concurrentes a la PokeAPI.
* Imprime el nombre, tipo(s), y estadísticas base de cada Pokémon.
* Maneja errores de solicitud a la API.

## Cómo usar

1. **Requisitos:** Asegúrate de tener Python 3 instalado y la librería `requests`. Puedes instalarla con pip:

   ```bash
   pip install requests
   ```

2. **Ejecutar el script:** Simplemente ejecuta el script `pokeAPI.py` desde tu terminal:

   ```bash
   python pokeAPI.py
   ```

## Detalles de Implementación

* **Clase `PokeAPI`:**  Esta clase hereda de `threading.Thread` y maneja la solicitud a la API para un Pokémon específico. El método `run()` realiza la solicitud HTTP GET y almacena la respuesta JSON en el atributo `pokemon`.

* **Hilos:** El script crea un hilo para cada Pokémon que se va a consultar. Esto permite que las solicitudes se realicen en paralelo, lo que reduce significativamente el tiempo de ejecución.

* **Bloqueo de hilos (threading_lock):** Se utiliza un `threading.Lock` para proteger la sección crítica del código donde se imprime la información del Pokémon. Esto evita que la salida se mezcle cuando múltiples hilos intentan imprimir al mismo tiempo.

* **Manejo de errores:** El script verifica el código de estado de la respuesta HTTP. Si el código no es 200 (OK), se imprime un mensaje de error.

## Posibles Mejoras

* **Manejo de excepciones más robusto:** Se podría implementar un manejo de excepciones más completo para capturar errores específicos, como problemas de conexión de red.
* **Configuración del número de hilos:**  Se podría permitir al usuario especificar el número de hilos a utilizar, en lugar de usar un valor fijo de 100.
* **Paginación:** Para obtener información sobre más de 100 Pokémon, se podría implementar la paginación utilizando los enlaces "next" y "previous" proporcionados por la PokeAPI.
* **Almacenamiento de datos:**  Se podrían guardar los datos obtenidos en un archivo (CSV, JSON, etc.) para su posterior análisis o uso.


## Ejemplo de Salida

```
NOMBRE: bulbasaur
TIPO: ['grass', 'poison']
ESTADISTICAS:
  Vida: 45
  Ataque: 49
  Defensa: 49
  Ataque especial: 65
  Defensa especial: 65
  Velocidad: 45

NOMBRE: ivysaur
TIPO: ['grass', 'poison']
ESTADISTICAS:
  Vida: 60
  Ataque: 62
  Defensa: 63
  Ataque especial: 80
  Defensa especial: 80
  Velocidad: 60
