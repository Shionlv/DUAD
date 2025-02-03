#Ejercicios
#2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#    1. Debe leer el archivo para importar los Pokémones existentes.
#    2. Luego debe pedir la información del Pokémon a agregar.
#    3. Finalmente debe guardar el nuevo Pokémon en el archivo.

#Mi RESPUESTA

import json

def pokemons(path_entrada):
    with open(path_entrada, 'r') as file:
        lines = json.load(file)

        pokemon_nuevo = {}
        name_english = input("Ingresa el nombre en inglés del Pokémon: ")
        type = input("Ingresa el tipo del Pokémon (por ejemplo, plant): ")

    while True:
        try:
            base_hp = int(input("Ingresa el HP base del Pokémon: "))
            break  
        except ValueError:
            print("Error: Debes ingresar un número entero para el HP.")
            continue  

    while True:
        try:
            base_attack = int(input("Ingresa el Attack base del Pokémon: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero para el Attack.")
            continue

    while True:
        try:
            base_defense = int(input("Ingresa el Defense base del Pokémon: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero para el Defense.")
            continue

    while True:
        try:
            base_sp_attack = int(input("Ingresa el Sp. Attack base del Pokémon: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero para el Sp. Attack.")
            continue

    while True:
        try:
            base_sp_defense = int(input("Ingresa el Sp. Defense base del Pokémon: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero para el Sp. Defense.")
            continue

    while True:
        try:
            base_speed = int(input("Ingresa el Speed base del Pokémon: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero para el Speed.")
            continue

    pokemon_nuevo = {
        "name": {
            "english": name_english
            },
            "type": [type],
            "base": {
                "HP": base_hp,
                "Attack": base_attack,
                "Defense": base_defense,
                "Sp. Attack": base_sp_attack,
                "Sp. Defense": base_sp_defense,
                "Speed": base_speed
                }
            }

    lines.append(pokemon_nuevo)

    with open(path_entrada, 'w') as file:
        json.dump(lines, file, indent=4)
    print(lines) #Esto lo puse como para poder ver en la terminal el resultado pero si se agrego el pokemon al archivo pokemons.json

pokemons("pokemons.json") 


#RESPUESTA 2!
#En este caso use chatgpt y le pregunte como podria hacer mas eficiente mi 
#codigo he hizo una funcion extra para llamar a la def obtener_entero() por cada input
#Para futuros ejercicios me parece una forma muy buena y logica que estare aplicando

import json

def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
            continue

def pokemons(path_entrada):
    try:
        with open(path_entrada, 'r') as file:
            lines = json.load(file)
    except FileNotFoundError:
        
        lines = []

    name_english = input("Ingresa el nombre en inglés del Pokémon: ")
    pokemon_type = input("Ingresa el tipo del Pokémon (por ejemplo, plant): ")

    base_hp = obtener_entero("Ingresa el HP base del Pokémon: ")
    base_attack = obtener_entero("Ingresa el Attack base del Pokémon: ")
    base_defense = obtener_entero("Ingresa el Defense base del Pokémon: ")
    base_sp_attack = obtener_entero("Ingresa el Sp. Attack base del Pokémon: ")
    base_sp_defense = obtener_entero("Ingresa el Sp. Defense base del Pokémon: ")
    base_speed = obtener_entero("Ingresa el Speed base del Pokémon: ")

    pokemon_nuevo = {
        "name": {
            "english": name_english
        },
        "type": [pokemon_type],
        "base": {
            "HP": base_hp,
            "Attack": base_attack,
            "Defense": base_defense,
            "Sp. Attack": base_sp_attack,
            "Sp. Defense": base_sp_defense,
            "Speed": base_speed
        }
    }

    lines.append(pokemon_nuevo)

    with open(path_entrada, 'w') as file:
        json.dump(lines, file, indent=4) 

    print("El Pokémon ha sido agregado exitosamente.")

pokemons("pokemons.json")