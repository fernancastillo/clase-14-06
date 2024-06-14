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
        descuento_salud=int(0.07*sueldo_bruto)
        descuento_afp=int(0.12*sueldo_bruto)
        sueldo_liquido=sueldo_bruto-descuento_salud-descuento_afp
        trabajador=[nombre_apellido, cargo, sueldo_bruto, descuento_salud, descuento_afp, sueldo_liquido]
        trabajadores.append(trabajador)
        print("TRABAJADOR REGISTRADO CON ÉXITO!")
    elif opc==1:
        if len(trabajadores)==0:
            print("No existen trabajadores, elija la opción 1")
        else:
            print("\tLISTA DE TRABAJADORES:")
            print("Tabajador\tCargo\tSueldo bruto\tDesc. Salud\tDesc. AFP\tLíquido a pagar")
            for t in trabajadores: #t es cada trabajador de la lista, t es una lista
                print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t{t[4]}\t\t{t[5]}")
    elif opc==2:
        if len(trabajadores)==0:
            print("No existen trabajadores, elija la opción 1")
        else:
            opc2=int(input("¿Qué cargo desea imprimir? (1:CEO, 2:DESARROLLADOR, 3:ANALISTA, 4:TODOS): "))
            if opc2==4:
                with open ("todos_trabajadores.txt", "w", newline="\n") as archivo:
                    for t in trabajadores:
                        texto=f"{t[0]} {t[1]} {t[2]} {t[3]} {t[4]} {t[5]}"
                        archivo.write(texto)
            else:
                with open ("trabajadores_por_cargo.txt","w") as archivo:
                    for t in trabajadores:
                        if opc2==t[1]:
                            texto=f"{t[0]} {t[1]} {t[2]} {t[3]} {t[4]} {t[5]}"
                            archivo.write(texto)
            print("Archivo creado con éxito!")

    else:
        print("Gracias por usar el programa, adios!")
        break
    time.sleep(3)