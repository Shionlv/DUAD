
#💪🏽 **Ejercicios SEMANA 4**

#Ya modifique las respuestas acorde al ejercicio, creo que quedo bien. 

#1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

#RESPUESTA

Nombre="Lee"
Apellido="Viquez"
Anios="edad"
edad= 31
lista= ["Osa", "Dakota", "Oso"]
lista2= ["Osa2", "Dakota2", "Oso2"]
numero_con_decimales=18.6
verdad=True
mentira=False

#1. string + string → ?

print(f"{Nombre} {Apellido}")
print("Hola " + "Adios")

#2. string + int → ?

print((f"{Anios}: {edad}"))

print("Edad " + str(31)) #str para pasar un int a string al hacer print

#3. int + string → ?

print(str(31) + " edad") #str para pasar un int a string al hacer print

#4. list + list → ?

print(lista + lista2)

#5. string + list → ?

print(f"Lista 1:  {lista}")

print("Lista 1: " + lista) #esto da error

#6. float + int → ?

print(9.9 + 1)

#7. bool + bool → ?
#No sabia que al hacer la suma de dos booleanos daba estos resultados en el print, ahora veo que True es 1 y False es 0
print(True + True)    # 2
print(True + False)   # 1
print(False + False)  # 0

#2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, 
# adulto joven, adulto, o adulto mayor.

#RESPUESTA

nombre=input("Escribe tu nombre: ")
apellido=input("Escribe tu apellido: ")
edad=int(input("Escribe tu edad: "))

if edad <= 2:
    print(f"Tiene {edad}, es un bebe que se llama {nombre} y se apellida {apellido}")
elif edad <= 10 and edad >= 3:
    print(f"Tiene {edad}, es un ninio que se llama {nombre} y se apellida {apellido}")
elif edad <= 13 and edad >= 10:
    print(f"Tiene {edad}, es un preadolecente que se llama {nombre} y se apellida {apellido}")
elif edad <= 19 and edad >= 13:
    print(f"Tiene {edad}, es un adolecente que se llama {nombre} y se apellida {apellido}")
elif edad <= 20 and edad >= 35:
    print(f"Tiene {edad}, es un adulto joven que se llama {nombre} y se apellida {apellido}")
elif edad <= 60 and edad >= 36:
    print(f"Tiene {edad}, es un adulto que se llama {nombre} y se apellida {apellido}")
else:
    print(f"Tiene {edad}, es un adulto mayor que se llama {nombre} y se apellida {apellido}")


#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

#RESPUESTA

import  random

numero_random=random.randint(1,11)

print("Adivina el numero del 1 al 10")

while True:
    numero_usuario=int(input("Ingresa un numero: "))
    if numero_random == numero_usuario:
        print("Acertaste")
        break
    else:
        print("Try again")

#Cree un programa que le pida tres números al usuario y muestre el mayor.

#RESPUESTA

numero1=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
numero3=int(input("Ingresa el tecer numero: "))

numeros_del_usuario=[numero1, numero2, numero3]

numero_mayor=max(numeros_del_usuario)

print(f"El numero mas alto de los tres ingresados es: {numero_mayor}")

#Dada `n` cantidad de notas de un estudiante, calcular:
#    1. Cuantas notas tiene aprobadas (mayor a 70).
#    2. Cuantas notas tiene desaprobadas (menor a 70).
#    3. El promedio de todas.
#    4. El promedio de las aprobadas.
#    5. El promedio de las desaprobadas.

#RESPUESTA

contador_de_nota = 1
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0
suma_notas_aprobadas = 0
suma_notas_desaprobadas = 0
suma_total_notas = 0

total_de_notas=int(input("Ingrese la cantidad de notas: "))

while contador_de_nota <= total_de_notas:
    nota_actual=int(input("Ingrese la nota: "))
    suma_total_notas += nota_actual

    if nota_actual < 70:
        cantidad_de_notas_desaprobadas +=1
        suma_notas_desaprobadas += nota_actual
    elif nota_actual > 70:
        cantidad_de_notas_aprobadas +=1
        suma_notas_aprobadas += nota_actual

    contador_de_nota += 1

if cantidad_de_notas_aprobadas > 0:
    promedio_de_notas_aprobadas = suma_notas_aprobadas / cantidad_de_notas_aprobadas
else:
    promedio_de_notas_aprobadas = 0

if cantidad_de_notas_desaprobadas > 0:
    promedio_de_notas_desaprobadas = suma_notas_desaprobadas / cantidad_de_notas_desaprobadas
else:
    promedio_de_notas_desaprobadas = 0

promedio_de_notas_total = suma_total_notas / total_de_notas


print(f"El estudiante aprobó: {cantidad_de_notas_aprobadas}")
print(f"Con un promedio de: {promedio_de_notas_aprobadas}")

print(f"El estudiante reprobó: {cantidad_de_notas_desaprobadas}")
print(f"Con un promedio de: {promedio_de_notas_desaprobadas}")

print(f"Promedio de todas las notas: {promedio_de_notas_total}")

#Para este ejercicio necesite ayuda ya que no entendia bien como hacer las suma de notas 1 por 1 y luego sumar la nota ingresada
#por el ususario, posteriormente tambien necesite ayuda para aplicar el condicional if/else y conseguir los promedios. Mas adelante tratare de hacerlo sin ayuda.


#Ejercicios de Pseudocódigo

#1. Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#    1. Si el precio es menor a 100, el descuento es del 2%.
#    2. Si el precio es mayor o igual a 100, el descuento es del 10%.

#RESPUESTA

precio_de_producto=int(input("Ingrese precio del producto: $"))

if precio_de_producto < 100:
        descuento= precio_de_producto * 2 /100
        precio_final=precio_de_producto - descuento
        print(f"El precio final del producto con el descuento es de:  ${precio_final}")

if precio_de_producto >= 100:
        descuento= precio_de_producto * 10 /100
        precio_final=precio_de_producto - descuento
        print(f"El precio final del producto con el descuento es de:  ${precio_final}")


#2. Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. 
# Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”.

#RESPUESTA

Tiempo_en_segundos=int(input("Ingrese el tiempo en segundos: "))

if Tiempo_en_segundos >= 600:
    print("El tiempo ingresado en mayor a 10 minutos")

if Tiempo_en_segundos <= 600:
    Tiempo_faltante= 600-Tiempo_en_segundos
    print(f"El tiempo ingresado en menor a 10 minutos y le faltan:  {Tiempo_faltante}  segundos para  llegar a 10 minutos")

#3. Cree un algoritmo que le pida un numero al usuario y muestre la suma de todos los números desde 1 hasta ese número.

#RESPUESTA

numero=int(input("Ingrese 1 numero: "))
suma=0

while numero > 0:
    suma += numero
    numero = numero - 1

print(f"La suma de todos los números desde el 1 hasta el numero ingresado es de: {suma}")

#Ejercicios Extra

#1. Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (`primero` y `segundo`) y los ordene de menor a mayor en dichas variables.

#RESPUESTA

numero_1=int(input("Ingrese un número 1: "))
numero_2=int(input("Ingrese un número 2: "))

if numero_1 > numero_2:
    numero_x = numero_1
    numero_1= numero_2
    numero_2 = numero_x

print(f"Los numeros ordenados son: {numero_1} y {numero_2}")

#2. Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos.

#RESPUESTA

velocidad=int(input("Ingrese la velocidad en km/h: "))

metros=0
segundos=0

metros = velocidad * 1000
segundos =  60 * 60
velocidad_m_s = metros / segundos

print(f"La velocidad en m/s es: {velocidad_m_s:.2f}")


#3. Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.

#RESPUESTA

hombres=0
mujeres=0
contador=1
cantidad_de_personas=int(input("Ingresa cantidad de personas en el grupo: ")) #Agregue esta variable y asi el usuario elige la cantidad de personas y asi no estar limitado a 6

while contador <= cantidad_de_personas:
    sexo=int(input("Ingrese 1 si es mujer o 2 si es hombre: ")) 
    if sexo==1:
        mujeres += 1
    elif sexo==2:
        hombres += 1
    elif sexo != 1 and sexo != 2:
        print("Ingresaste un numero erroneo")
        continue #Use "continue" para evitar que el contador sumara 1 cuando el usuario ingresara un numero erroneo y el bucle comenzara de nuevo
    contador += 1
    

porcentaje_mujeres = (mujeres / 6) * 100    
porcentaje_hombres = (hombres / 6) * 100

print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f} %")
print(f"Porcentaje de hombres: {porcentaje_hombres:.2f} %") 