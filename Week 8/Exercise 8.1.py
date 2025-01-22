
#💪🏽 **Ejercicios**

#1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def canciones(path_entrada, path_salida):
    with open(path_entrada, 'r') as file:

        lines = file.readlines()
        
        lines.sort()
        
    with open(path_salida, 'w') as file:
        file.writelines(lines)
    
    print(f"Canciones ordenadas alfabeticamente en otro archivo: {path_salida}")

path_entrada = r'canciones.txt'
path_salida = r'canciones_ordenadas.txt'

canciones(path_entrada, path_salida)