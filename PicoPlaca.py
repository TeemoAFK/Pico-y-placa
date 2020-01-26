Placa_auto=input("Ingrese la placa de su vehiculo: ")

Dia=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
Placa=["1-2","3-4","5-6","7-8","9-0","N/A","N/A"]
fecha=int(input("Ingresa un dia del año! (1-365)"))
hora=int(input("Ingrese una hora: "))

if(fecha>0 and fecha <366):
    if(fecha <7):
        print(Dia[fecha-1]+":"+Placa[fecha-1])
        if(hora>7 or hora<9 or hora>17 or hora<19):
            print("No esta permitido circular")
        else:
            print("Circula libremente")

    elif(fecha % 7==0):
        print(Dia[6]+":"+Placa[6])

    else:
        print(Dia[(fecha-1)%7]+":"+Placa[(fecha-1)%7])

else:
    print("Favor ingresa un dia valido")