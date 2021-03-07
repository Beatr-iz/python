# Entrada de datos
print ("Ingresa tu nombre completo")
nombre = input()
print ("Ingresa RFC")
RFC = input()
print ("Ingresa No. de empleado")
Num empleado = int(input())
print ("Ingresa el salario por quincena")
sueldoquincena = float(input())
print ("Ingresa las horas trabajadas por quincena")
hrsmes = int(input())
print ("Ingresa los dias trabajados por quincena")
diasquincena = int(input())
print ("Ingresa el numero de dias de inasistencia por incapacidad")
diasincapacidad = int(input())
print ("Ingresa el numero de faltas de esta quincena")
faltas = int(input())
print ("Ingresa el numero de retardos de esta quincena")
retardos = int(input())

# Operaciones o calculos matematicos:

#absentismo con/sin justificacion ? 
if (faltas == 1):
    faltasinjusti = (sueldodia * 0.83)*1 + (sueldodia * 5)
elif (faltas == 2):
    faltasinjusti = (sueldodia * 0.83)*2 + (sueldodia * 4)
 elif (faltas == 3):
    faltasinjusti = (sueldodia * 0.83)*3 + (sueldodia * 3)
 else:
    print ("Incumplimiento al contrato")


sueldosemanal = sueldoquincena / 2
sueldodia = sueldosemanal / 7

aguinaldo = (sueldodia * 15) / 365
primavacacional = sueldodia * diasañostrabajados / 365
SBC = sueldodia + aguinaldo + primavacacional

UMA = 89.62 
cuotafija = (UMA * (UMA*3)) * diasquincena * diasincapacidad)


if SBC > (UMA *3):
excsbcpatron = (((UMA * 3)  - SBC) * 1.10%)*(diasquincena- diasincapacidad)
else: #si quiero especificar una condicion para cuando el sbc sea mayor
excsbcpatron = 0 
excsbctrabaj = (((UMA * 3)  - SBC) * .40%)*(diasquincena- diasincapacidad)

#como puedo redondear a dos decimales?
prestacionesdineropat = (SBC*.70)* (diasquincena - diasincapacidad)

prestacionesdinerotrab = (SBC*.25)* (diasquincena - diasincapacidad)

# fundament Art. 25 LSS
gastosmedpensionadospatr= (SBC *1.050%) * (diasquincena - diasincapacidad)

gastosmedpensionadostrab = (SBC *0.375%) * (diasquincena - diasincapacidad)

# fundament Art. 112 - 150 LSS

diasnetos =diasquincena - faltas - diasincapacidad
invalidezvidapatr =SBC * 1.750% * diasnetos
invalidezvidatrab =SBC * 1.13065% * diasnetos

# fundament Art. 73 LSS RIESGO DE TRABAJO

RT = (SBC * 1.13065%) *diasnetos

# Art. 11 LSS 
guarderias = SBC * 1% * diasnetos

totalcuotaspatron = cuotafija + excsbcpatron + prestacionesdineropat + gastosmedpensionadospatr +invalidezvidapatr+RT+guarderias
totalcuotastrabaj = excsbctrabaj + prestacionesdinerotrab + gastosmedpensionadostrab + invalidezvidatrab 


sueldodia = sueldoquincena/15
sueldohora = sueldodia / 8  #si quiero un empleado trabaja 4 hrs extras en un dia ??
if (hrsquincena > 96 and hrsquincena <= 105):   
hrsextras2 = hrsquincena - 96
hrsextrasdobles = hrsextras2 * sueldohora * 2
elif (hrsquincena > 105):
hrsextras3 = hrsquincena - 105
hrsextrastriples = hrsextras3 * sueldohora * 3



        
SM = 141.7    #puedo hacer una funcion para que se agregue una tabla con la informacion del salario minimo?
if sueldodia > SM:
    ingresomensual= sueldoquincena + (hrsextrasdobles + hrsextrastriples * .50)
    else:
        ingresomensual= sueldoquincena + 0
    
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

        if(retardos == 0):
    bono = sueldoquincena + 500
else:
    print("No se obtuvo bono de puntualidad")       

         fondoahorro = sueldoquincena * .8%
         valesdespensa = sueldoquincena * .10% #puedo agregar una funcion para que en quincena de fin de mes se agregue este plus?
      

    # Imprimir o mostrar en pantalla
        print("Importe:"+ importe)
        print("Bono de puntualidad:"+ bono)
        print("Descuento:"+ descuento)
        print("Sueldo:"+ ingresosobt)
        print("ISR" + ISR)
        



