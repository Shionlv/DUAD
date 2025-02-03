#💪🏽 **Ejercicios**

#1. Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el 
# nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.


numero_actual=0  

def calculadora(): #Primer funcion que pide los datos y verifica exceptions

    global numero_actual # Variables con global ya que necesito que estas variables se puedan usar en la funcion Calculo()

    print("Soy una calculadora sencilla.") #Un nombre sencillo
    print("Puedo solamente sumar, restar, multiplicar y dividir.") #Una breve explicacion de lo que se puede hacer
    print(f"Número actual: {numero_actual}") #Aqui es para ver el numero actual es cero

    calculo = ""  # Variable local

    while True:
        try:
            numero_actual = int(input("Ingresa el primer número (no puede ser 0): "))
            if numero_actual == 0:
                print("El número no puede ser 0. Intente de nuevo.")
                continue
        except ValueError as error:
            print(f"Error: {error}")
            continue

        try:
            calculo = input("Ingresa '+', '-', '*', '/': ")

            if calculo not in ['+', '-', '*', '/']: #Si el usuario ingreso algo que no esta en lista el programa avisa del error y comienza de nuevo
                raise ValueError("Dato no valido. Ingrese una opción disponible.")
            
            if calculo == 'borrar':
                numero_actual = 0
                print("Resultado borrado. Número actual reiniciado a 0.")
                continue  # Reinicia el ciclo para pedir nuevos datos

        except ValueError as error:
            print(f"Error: {error}")
            continue

        try:
            numero_actual2 = int(input("Ingresa el segundo número: "))
            if calculo == "/" and numero_actual2 == 0:  # Validación específica para la división entre cero
                raise ZeroDivisionError("No se puede dividir entre cero. Intente con otro número.")
        except ValueError as error:
            print(f"Hubo un error al convertir este string a número: {error}!")
            continue
        except ZeroDivisionError as error:
            print(error)
            continue

        return calculo, numero_actual2 #Esto va ser el parametro de la siguiente funcion donde se va hacer los calculos


def calculo (calculo, numero_actual2): #Segunda funcion que hace los calculos de los datos recolectados en la primera funcion calculadora()

        if calculo == "+":
            print(f"{numero_actual} + {numero_actual2}: {numero_actual + numero_actual2}")
        elif calculo == "-":
            print(f"{numero_actual} - {numero_actual2}: {numero_actual - numero_actual2}")
        elif calculo == "*":
            print(f"{numero_actual} * {numero_actual2}: {numero_actual * numero_actual2}")
        elif calculo == "/":
            if numero_actual2 != 0:
                print(f"{numero_actual} / {numero_actual2}: {numero_actual / numero_actual2}")


def main():  # Función principal que llama a las otras
    while True: #Bucle para pregunta al usuario si quiere hacer otro calculo con otros numeros, esta parte viene siendo el borra resultado pero con un bucle para volver a empezar
        operacion, numero_actual2 = calculadora()
        calculo(operacion, numero_actual2)
        continuar = input("¿Desea realizar otra operación? (yes/no): ").lower() #.lower() para que sea indiferente si pongo YES o yes
        if continuar != 'yes':
            print("Bueno se acabo, adios")
            break

if __name__ == "__main__":
    main()

#Ejercicio extra que me invente.

#Quiero crear un programa que pida al usuario la lista de productos que compra en el supermercado cada mes la lista debe tener:
#1.Nombre del producto
#2.Precio del producto
#3:Cantidad comprada
#4.Total de gastos
#Luego debo se deben almacenar estos datos e un diccionario con cada producto con su respectivo precio.

#El programa debe mostrar el gasto mensual al final
#Debo usar def, bucles, exeptions, listas, diccionarios, condicionales

#Esta practica la hice mayormente usando mi logica y lo he aprendido hasta ahora a base de prueba y error. 
#Me gustaria continuar con esta idea como proyecto y hacerlo una app o pagina en algun momento.

lista_de_productos = []
lista_de_precios = []
lista_con_precios = {}

def cantidad_de_compras(): #Primer funciona para saber cuantas cosas compro
    while True: 
        try:
            cantidad_de_compras = int(input("¿Cuántos productos compraste? (1-100): ")) #Minimo de 1 maximo de 100
            if 1 <= cantidad_de_compras <= 100: #if para comprobar si esta dentro del ranto de 1 a 100
                return cantidad_de_compras #En caso de estarlo retorna el numero ingresado
            else:
                print("Ingresa un número entre 1 y 100.") #Si ingresa un numero mayor a 100 o negativo se repite
        except ValueError as error: #Si ingresa un string avisa del error y se repite
            print(f"Error: {error}. Ingresa un número válido.")


def ingresar_productos(cantidad_de_compras): #Segunda funcion para saber los nombres y precios
    productos_comprados = 0 #Un contador basicamente
    while productos_comprados < cantidad_de_compras: #El bucle se repite igual a la cantidad de productos comprados, esto se definio en la primera funcion
        producto = input(f"Ingresa el nombre del producto {productos_comprados + 1}: ")#Se agrega esto {productos_comprados + 1} para saber el nombre del producto y el nunmero del mismo

        while True: #El bucle se repite igual a la cantidad de productos comprados
            try:
                precio_producto = float(input(f"Ingresa el precio del producto '{producto}': "))
                break
            except ValueError as error:
                print(f"Error: {error}. Ingresa un precio válido.")

        lista_de_productos.append(producto) #Se agrega el nombre del producto a la lista vacia
        lista_de_precios.append(precio_producto) #Se agrega el precio a la lista vacia
        productos_comprados += 1 

    lista_con_precios = dict(zip(lista_de_productos, lista_de_precios)) #dic() para convertir a diccionario y zip para el nombre y precio
    gasto_total=sum(lista_de_precios) #Variable para sumar la lista de precios

    return lista_con_precios, gasto_total 

cantidad = cantidad_de_compras() #Lllamada de la primer funcion
productos_con_precios, gasto_total = ingresar_productos(cantidad) #Llamada a la segunfa funcion
print(f"La lista de productos con sus respectivos precios es de: {productos_con_precios}") #El diccionario que se armo 
print(f"El gasto total es de: {gasto_total:.2f}") #:.2f para que el resultado solo tenga 2 decimales


#Este es el codigo modificado por chatgpt para hacerlo mas simple, no sabia como hacerlo yo mas simple asi que le pedi que lo hiciera a ver que pasaba,
#es basicamente lo mismo pero reduce el codigo al quitar la necesidad de usar dos listas y solo meter los precios y productos de una vez en dict, 
#ahora veo como se podria resumir para que sea mas eficiente y rapido

def obtener_cantidad_de_compras():
    while True:
        try:
            cantidad_de_compras = int(input("¿Cuántos productos compraste? (1-100): "))
            if 1 <= cantidad_de_compras <= 100:
                return cantidad_de_compras
            print("Por favor, ingresa un número entre 1 y 100.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def ingresar_productos(cantidad_de_compras):
    productos_con_precios = {} 

    for _ in range(cantidad_de_compras):
        producto = input("Ingresa el nombre del producto: ")
        while True:
            try:
                precio_producto = float(input(f"Ingresa el precio del producto '{producto}': "))
                break 
            except ValueError:
                print("Por favor, ingresa un precio válido.")

        productos_con_precios[producto] = precio_producto #No sabia que asi se podia meter al diccinarios la clave-valor en orden

    return productos_con_precios


cantidad = obtener_cantidad_de_compras()
productos_con_precios = ingresar_productos(cantidad)
gasto_total = sum(productos_con_precios.values()) #Esta forma de usar sum para sumar y .values() para sumar solamente los valores del dict es nueva para mi

print(f"La lista de productos con sus respectivos precios es: {productos_con_precios}")
print(f"El gasto total es: {gasto_total:.2f}")