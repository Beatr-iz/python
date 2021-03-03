
 # Entrada de datos
print ("Ingresa el numero de litros de agua")
numero1 = int(input())
print ("Ingresa tu segunda calificacion")
numero2 = int(input())
print ("Ingresa tu tercera calificacion")
numero3 = int(input())

# Operaciones o calculos matematicos
suma = numero1 + numero2 + numero3
promedio = suma / 3

# Imprimir o mostrar en pantalla
print(f"El promedio = {promedio}")


if (promedio <5):
    print("Reprobado")
else:
    print("Aprobado")