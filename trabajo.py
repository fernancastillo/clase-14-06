import os, time
trabajadores=[]
while True:
    print("MENÚ TRABAJADORES")
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir planilla de suldos")
    print("4. Salir del programa")
    opc=int(input("Ingrese opción: "))
    os.system("cls")
    if opc==1:
        print("REGISTRAR TRABAJADOR")
        nombre_apellido=input("Ingrese nombre y apellido: ")
        cargo=int(input("Ingrese el cargo (1. CEO, 2. Desarrollador, 3. Analista): "))
        sueldo_bruto=int(input("Ingrese sueldo bruto: "))
        descuento_salud=0.07*sueldo_bruto
        descuento_afp=0.12*sueldo_bruto
        sueldo_liquido=sueldo_bruto-descuento_salud-descuento_afp
        trabajador=[nombre_apellido, cargo, sueldo_bruto, descuento_salud, descuento_afp, sueldo_liquido]
        trabajadores.append(trabajador)
        print("TRABAJADOR REGISTRADO CON ÉXITO!")
    elif opc==1:
        pass
    elif opc==2:
        pass
    else:
        print("Gracias por usar el programa, adios!")
        break
    time.sleep(3)