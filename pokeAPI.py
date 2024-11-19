import threading
import requests
import json

# Diccionario para tener una estructura de los datos del pokemon
pokemon_dict = {
    "Nombre": "",
    "Tipo": 0,
    "Estadisticas": {
        "Vida": 0,
        "Ataque": 0,
        "Defensa": 0,
        "Ataque especial": 0,
        "Defensa especial": 0,
        "Velocidad": 0
    },
}

threading_lock = threading.Lock()

class PokeAPI(threading.Thread):
    def __init__(self, url):
        # Creacion del hilo
        threading.Thread.__init__(self)
        self.pokemon = None
        self.url = url

    # Ejecución del hilo
    def run(self):
        # Se realiza la petición a la API
        response = requests.get(url)
        # Se obtiene el JSON de la respuesta
        if response.status_code == 200:
            self.pokemon = response.json()
        else:
            print(f"Error en la solicitud: {response.status_code}")

    def get_pokemon(self):
        return self.pokemon
    
if __name__ == "__main__":
    hilos = []
    for i in range(1, 101):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        hilo = PokeAPI(url)
        hilo.start()
        hilos.append(hilo)

    for hilo in hilos:
        hilo.join()
        pokemon = hilo.get_pokemon()
        tipos = [pokemon['types'][t]['type']['name'] for t in range(len(pokemon['types']))]
        with threading_lock:
            print(f"NOMBRE: {pokemon['name']}")
            print(f"TIPO: {tipos}")
            print("ESTADISTICAS:")
            print(f"  Vida: {pokemon['stats'][0]['base_stat']}")
            print(f"  Ataque: {pokemon['stats'][1]['base_stat']}")
            print(f"  Defensa: {pokemon['stats'][2]['base_stat']}")
            print(f"  Ataque especial: {pokemon['stats'][3]['base_stat']}")
            print(f"  Defensa especial: {pokemon['stats'][4]['base_stat']}")
            print(f"  Velocidad: {pokemon['stats'][5]['base_stat']}")
            print("\n")
    


