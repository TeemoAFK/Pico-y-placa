Dia=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
Placa=["1-2","3-4","5-6","7-8","9-0","N/A","N/A"]

numero=int(input("Ingresa un dia del año! (1-365)"))

if(numero>0 and numero <366):
    if(numero <7):
        print(dia[numero-1]+)":"+Placa[numero-1])

    elif(numero % 7==0):
        print(Dia[6]+":"+Placa[6])

    else:
        print(Dia[(numero-1)%7)]+":"+Placa[(numero-1)%7])

else:
    print("Favor ingresa un dia del 1 al 365")