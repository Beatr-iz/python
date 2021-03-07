 
 
 # Entrada de datos
print ("Ingresa tu primer calificacion")
numero1 = float(input())
print ("Ingresa tu segunda calificacion")
numero2 = float(input())
print ("Ingresa tu tercera calificacion")
numero3 = float(input())

# Operaciones o calculos matematicos
suma = (numero1 + numero2 + numero3)
promedio = (suma / 3)

# Imprimir o mostrar en pantalla
print("El promedio es" + promedio)

if (promedio <5):
    print("Reprobado")
else:
    print("Aprobado")