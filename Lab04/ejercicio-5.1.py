contador = 0
suma = 0
while True:
    numero = input("Ingrese un número:")
    if (numero == "salir"):
        break
    else:
        contador = contador + 1 
        suma = suma + int(numero)
        promedio = suma / contador
print("contador;", contador)
print("suma;", suma)

print("promedio;", promedio)