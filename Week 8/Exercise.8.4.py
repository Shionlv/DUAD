#💪🏽 **Ejercicios**

#1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#    1. Debe incluir:
#        1. Nombre
#        2. Género
#        3. Desarrollador
#        4. Clasificación ESRB 
#    2. Ejemplo de archivo final:
#        nombre,genero,desarrollador,clasificacion
#        Grand Theft Auto IV,Accion,Rockstar Games,M
#        The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
#        Tony Hawk's Pro Skater 2,Deportes,Activision,T

import csv

def ingresar_datos(): #creo que no hace falta un parametro ya que no le vamos a ingresar nada
    juegos = [] #lista vacia para almacenar los juegos
    
    while True: #Un bucle while true para que nunca termine hasta que el usuario quiera escribiendo "stop"
        nombre = input("Ingresa el nombre del juego (o 'Stop' para terminar): ") 
        
        if nombre.lower() == "stop": #.lower() por si acaso el usuario escribe en mayusculas
            break #Un if con un break al principio para dar la opcion de terminar de escribir datos de juegos 
        
        #inputs de los demas datos que se solicitan para el archivo CSV
        genero = input("Ingresa el género del juego: ")
        desarrollador = input("Ingresa el desarrollador: ")
        clasificacion = input("Ingresa la clasificación (ETMA): ")
        
        juego = { #Dict en el cual se va ir recopilando cada juego
            'Nombre': nombre,
            'Género': genero,
            'Desarrollador': desarrollador,
            'Clasificación': clasificacion,
        }
        juegos.append(juego) #Append para ingresar los datos solicitados al dict
    return juegos         # Agregar el diccionario con los datos del videojuego a la lista 'juegos'

def guardar_en_csv(file_path, datos):
    headers = ['Nombre', 'Género', 'Desarrollador', 'Clasificación']
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(datos)
    
    print(f"Juegos guardados en {file_path}")


def main():
    juegos = ingresar_datos()
    guardar_en_csv('listadejuegos.csv', juegos)  

main()


#2. Lea sobre el resto de métodos del módulo `csv` [aqui](https://docs.python.org/es/3/library/csv.html) y cree una version alternativa del ejercicio de 
# arriba que guarde el archivo separado por *tabulaciones* en vez de por *comas*.
#    1. Ejemplo de archivo final:
#        
#        nombre	genero	desarrollador	clasificacion
#        Grand Theft Auto IV	Accion	Rockstar Games	M
#        The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
#         Tony Hawk's Pro Skater 2	Deportes	Activision	T


def guardar_en_csv(file_path, datos):
    headers = ['Nombre', 'Género', 'Desarrollador', 'Clasificación']
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t') #Para que el CSV se separe en tabulaciones y no por comas solo debo agregar el argumento delimiter='\t'
        writer.writeheader()
        writer.writerows(datos)
    
    print(f"Juegos guardados en {file_path}")