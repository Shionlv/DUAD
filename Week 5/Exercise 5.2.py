#💪🏽 **Ejercicios**

#1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#    - `nombre`
#    - `numero_de_estrellas`
#    - `habitaciones`
#- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
#    - `numero`
#    - `piso`
#    - `precio_por_noche`

hotel={"Nombre": "Lee's Place", 
"Numero de estrellas": 5, 
"habitaciones":[
    {"numero": 1, "piso": 1, "precio": 200},
    {"numero": 2, "piso": 2, "precio": 300},
    {"numero": 3, "piso": 3, "precio": 400}]
}
print(hotel["habitaciones"][1])


#2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#    1. Ejemplos:
#    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
#    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
#    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`

list_1=["Nombre", "Apellido", "edad", "Ingresos"]
list_2=["Lee", "Viquez", 31, 5000]

dictionary={}

for i in range(len(list_1)):
    dictionary[list_1[i]]=list_2[i] #Elimine los [] de list_2, me parece que ya quedo bien

print(dictionary)

#2. Cree un programa que use una lista para eliminar keys de un diccionario.
#    1. Ejemplos:
#    2. `list_of_keys = [’access_level’, ‘age’]`
#    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
#    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`

list_3=["edad", "Ingresos"]

diccionario={"Nombre": "Lee", "Apellido":"Viquez", "edad": 31, "Ingresos": 5000}

for j in list_3:
    diccionario.pop(j)

print(diccionario)


#⭐ Ejercicios Extra

#1. Dada una lista de ventas con la siguiente información:
#`date`
#`customer_email`
#`items`
#Y cada item teniendo la siguiente información:
#`name`
#`upc`
#`unit_price`
#Cree un diccionario que guarde el total de ventas de cada UPC.


ventas=[ #esta primer parte la pude hacer solo
    {
        "date": "28/12/24",
        "customer email": "chuca@watata.com",
        "items": [
            {"name":"Fotografias 1","upc":"Paquete/100","unit_price": 500 },
            {"name":"Fotografias 2","upc":"Paquete/200","unit_price": 600 },
            {"name":"Fotografias 3","upc":"Paquete/300","unit_price": 700 },
            ],
        },
    ]

total_de_ventas={} #Esta seguda parte si necesite ayuda

for o in ventas:
    for item in o["items"]: 
        upc = item["upc"]
        precio = item["unit_price"]

        if upc in total_de_ventas:
            total_de_ventas[upc] += precio
        else:
            total_de_ventas[upc] = precio

total_de_ventas = {}

for o in ventas:
    for item in o["items"]:  
        upc = item["upc"]
        precio = item["unit_price"]

        if upc in total_de_ventas:
            total_de_ventas[upc] += precio
        else:
            total_de_ventas[upc] = precio

print(total_de_ventas)
