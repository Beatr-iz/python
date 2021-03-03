# Entrada de datos
print ("Ingresa tu nombre completo")
nombre = int(input())
print ("Ingresa RFC")
RFC = int(input())
print ("Ingresa No. de empleado")
Num empleado = int(input())
print ("Ingresa el sueldo por hora")
sueldohora = int(input())
print ("Ingresa las horas trabajadas por semana")
hrstrabajadas = int(input())
print ("Ingresa el numero de faltas por semana")
faltas = int(input())
print ("Ingresa el numero de retardos por semana")
retardos = int(input())

# Operaciones o calculos matematicos

sueldodia = sueldohora * 8

sueldosemanal = sueldodia * 7


if (faltas > 0 and = 1):

    faltas = (sueldosemanal / 5) * 4

elif (faltas = 2):
    
    faltas = (sueldosemanal / 5) * 3

 elif (faltas = 3):

    faltas = (sueldosemanal / 5) * 3 

 else 
    print ("Solicitar justificacion en RH")



if (hrstrabajadas > 40 and <= 49):
    print("Hay horas extras")

hrsextras = hrstrabajadas - 40:

sueldohrextra = hrsextras * sueldohora * 2:

importe (sueldohora * (hrstrabajadas + hrsextra))


if(retardos < = 0):
            bono = importe + 500
            print ("Felicitaciones obtuviste bono de puntualidad")

        retardos = sueldohora

        elif(retardos > = 1 and retardos < = 5):
            descuento = retardos * .50
        
        elif(retardos > = 6 and retardos < = 10):
            descuento= 250 + ((retardos-5) * 75)
        
        elif(retardos > = 11 and retardos < = 15):
            descuento= 625 + ((retardos-10) * 100)
       
       

        ingresosobt = (importe + hrsextra) - descuento
        
         fondoahorro = sueldomensual * 8%
         valesdespensa = sueldomensual * 10%
         ingresomensual = (ingresosobt * 30) + valesdespensa - fondoahorro
        
        if (ingresomensual > 0.01 and < 578.52):
            
            excedente = ingresomensual - 0.01

            impuestomarginal = excedente X 1.92% 

            ISR = impuestomarginal + 0

            
         elif (ingresomensual > 578.53 and < 4910.18):
            
            excedente = ingresomensual - 578.53

            impuestomarginal = excedente X 6.40% 

            ISR = impuestomarginal + 11.11

         elif (ingresomensual > 4910.19 and < 8629.20):
            
            excedente = ingresomensual - 4910.19

            impuestomarginal = excedente X 10.88% 

            ISR = impuestomarginal + 288.33

        elif (ingresomensual > 8629.21 and < 10031.07):
            
            excedente = ingresomensual - 8629.21

            impuestomarginal = excedente X 16% 

            ISR = impuestomarginal + 692.96

        elif (ingresomensual > 10031.08 and < 12009.94):
            
            excedente = ingresomensual - 10031.08

            impuestomarginal = excedente 17.92% 

            ISR = impuestomarginal + 917.26

        elif (ingresomensual > 12009.95 and < 24222.31):
            
            excedente = ingresomensual - 12009.95

            impuestomarginal = excedente 23.36% 

            ISR = impuestomarginal + 1271.87

        elif (ingresomensual > 24222.32 and < 38177.69):
            
            excedente = ingresomensual - 24222.32

            impuestomarginal = excedente 23.52% 

            ISR = impuestomarginal + 3880.44

         elif (ingresomensual > 38177.70 and < 72887.50):
            
            excedente = ingresomensual - 38177.70

            impuestomarginal = excedente 30% 

            ISR = impuestomarginal + 7162.74

            elif (ingresomensual > 72887.51 and < 97183.33):
            
            excedente = ingresomensual - 72887.51

            impuestomarginal = excedente 32% 

            ISR = impuestomarginal + 17575.69

            elif (ingresomensual > 97183.34 and < 297435.02):
            
            excedente = ingresomensual - 97183.34

            impuestomarginal = excedente 34% 

            ISR = impuestomarginal + 25350.35

            elif (ingresomensual > monto):

            monto = > 291550.01
            excedente = ingresomensual - monto

            impuestomarginal = excedente 35% 

            ISR = impuestomarginal + 91435.02

        
    # Imprimir o mostrar en pantalla
        print("Importe:"+ importe)
        print("Bono de puntualidad:"+ bono)
        print("Descuento:"+ descuento)
        print("Sueldo:"+ ingresosobt)
        print("ISR" + ISR)
        



