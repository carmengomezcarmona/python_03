#listas
mochila = ["espada", "pan", "escudo"]
print(mochila[2])

mochila.append("arco")
print(mochila)

del mochila[1]
print(mochila)

lista = []
print(lista)
lista.append(4)
print(lista)
lista.append(10)
print(lista)
lista = [
    [1, 2, 3],
    [4, 5, 6]
]
print(lista)
print(lista[0])
print(lista[0][1])

#tupla
print()
posicion = (4, 7, 2)
print(posicion)

#set
print()
animales = {
"gato",
"perro",
"gato",
"gato",
"conejo"
}
print(animales)

#diccionarios
print()
inventario = {
"espada": 2,
"pan": 8,
"poción": 1
}
print(inventario)
print(inventario["pan"])
inventario["pan"] = 25
print(inventario["pan"])

