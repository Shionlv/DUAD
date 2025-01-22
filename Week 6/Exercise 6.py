#💪🏽 **Ejercicios**

#1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def first ():
    print("Se me complican las funciones")


def main ():
    first()
    print("Espero entender rapido")


main()

#2. Experimente con el concepto de scope:
#    1. Intente accesar a una variable definida dentro de una función desde afuera.
#    2.  Intente accesar a una variable global desde una función y cambiar su valor.

variable_global=2025 #litetal es una varibale global

def variables ():
    variable=1993 #Esta en local al estar dentro de le funcion
    variable_global=2026 #Esta en local al estar dentro de le funcion
    print(f"{variable} y {variable_global}")

print(variable_global) 

variables() #Al hacer print veo que a pesar de que hay dos variables bajo el mismo 
#nombre ambas no se afectan al ser un global y otra loca


#3. Cree una función que retorne la suma de todos los números de una lista.
#    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41


def suma (la_lista):
    return print(f"La suma de los numeros es de: {sum(la_lista)}") 
#Use sum dentro del print que esta dentro del return para sumar la lista que esta 
#fuera de la funcion

lista_de_numeros=[4, 6, 2, 29]
suma(lista_de_numeros)


#4. Cree una función que le de la vuelta a un string y lo retorne.
#    1. Esto ya lo hicimos en iterables.
#    2. “Hola mundo” → “odnum aloH”

def string(palabras):
    resultado = " "  #un string vacio para almacenar "palabras"
    for i in range(len(palabras)-1, -1, -1): #para que el bucle se lea al reves
        resultado += palabras[i]  #para que se vaya almacenando letra por letra al reves
    
    return resultado  

alreves = string("Hola, me llamo Lee")
print(alreves) #Ahora si el resultado es: eeL omall em ,aloH
#La verdad no habia entendido el ejercicio

#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def mayus_minus(texto):
    mayusculas = 0
    minusculas = 0

    for caracter in texto:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1

    return mayusculas, minusculas

texto = "I HATE Sushi"
mayus, minus = mayus_minus(texto)
print(f"Cantidad de Mayúsculas: {mayus}, Cantidad de Minúsculas: {minus}")


#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def ordenar (texto1): #En prinpcio pense que tenia que hacer lista1 = list(texto1) pasar el str a list pero me dio error 
    lista1= texto1.split(", ") #split para dividir las palabras
    lista1.sort() #Para order la lista
    texto1="-".join(lista1) #join para unirlas y separarlas con un - tambien lo tuve que buscar
    return texto1

llamada=ordenar("Osa, Oso, Dakota, Dog, Pet, Cat, Lion, Capybara, Astronauta")
print(llamada)


#7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). 
# Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no

#Con este ejercicio estuve todo el 31 de diciembre tratando de completarlo buscando la logica matematica para saber si un numero es primo o no y como aplicar 
#esto a codigo pero por mas que le puse mente y trate de hacerlo solo pues no lo logre. Asi que gran parte del ejercicio fue con ayuda, pienso hacerlo de nuevo
#luego.

def primo(n):
    # Caso base: Si el número es menor o igual a 1 no es primo
    if n <= 1:
        return False
    # El 2 es primo
    if n == 2:
        return True
    # Si el número es par y mayor que 2, no es primo
    if n % 2 == 0:
        return False
    # Comprobar si n tiene algún divisor entre 3 y sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def primos(lista):
    primos_encontrados = []
    for numero in lista:
        if primo(numero):
            primos_encontrados.append(numero)
    return primos_encontrados

numeros_primos = [1, 2, 3, 4, 5, 6, 7, 8]

resultado = primos(numeros_primos)

print(resultado)