
# 1. Función que saluda con nombre y edad
def saludar(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años."

# 2. Función para calcular el promedio de 3 notas
def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# 3. Función para saber si un número es par o impar
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

# 4. Lista de comidas favoritas y recorrido con for
comidas = ["pizza", "sushi", "pastas", "tacos"]
for comida in comidas:
    print(f"Me gusta comer {comida}")

# 5. Contar del 1 al 10 con while
i = 1
while i <= 10:
    print(i)
    i += 1

# 6. While que pide un número hasta que el usuario escriba "salir"
# (comentado para evitar bucle en ejecución)
# while True:
#     entrada = input("Escribe un número o 'salir' para terminar: ")
#     if entrada.lower() == "salir":
#         break
#     print(f"Escribiste: {entrada}")

# 7. Función que cuenta cuántos elementos de una lista son mayores a 5
def contar_mayores_a_cinco(lista):
    contador = 0
    for numero in lista:
        if numero > 5:
            contador += 1
    return contador

# 8. Diccionario con datos personales
mi_info = {
    "nombre": "Adelem",
    "edad": 25,
    "ciudad": "Santiago"
}
# Acceder a un valor
print("Edad:", mi_info["edad"])
# Agregar un nuevo valor
mi_info["color_favorito"] = "azul"
print(mi_info)
