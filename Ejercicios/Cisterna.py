
 # Entrada de datos
print ("Ingresa el numero de litros de agua")
nivelagua = int(input())

# Operaciones o calculos matematicos

if (nivelagua == 0):
print("Hay fuga en la cisterna")
elif(nivelagua > 0 and < 2):
print("Encender bomba de agua")
elif(nivelagua > 2 and < 4):
print("Acelerar bomba de agua")
elif(nivelagua > 4 and < 6):
print("Bomba de agua trabajando")
elif(nivelagua > 6 and < 8):
print("Desacelerar bomba de agua")
elif(nivelagua > 8 and < 10):
print("Desacelerar bomba de agua")
else :
print("Desbordamiento de agua")