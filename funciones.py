trabajadores=[]
cargos=("CEO","DESARROLLADOR","ANALISTA")
def opcion_1():
    print("REGISTRAR TRABAJADOR")
    nombre_apellido=input("Ingrese nombre y apellido: ")
    cargo=int(input("Ingrese el cargo (1. CEO, 2. Desarrollador, 3. Analista): "))
    sueldo_bruto=int(input("Ingrese sueldo bruto: "))
    descuento_salud=int(0.07*sueldo_bruto)
    descuento_afp=int(0.12*sueldo_bruto)
    sueldo_liquido=sueldo_bruto-descuento_salud-descuento_afp
    trabajador=[nombre_apellido, cargos[cargo-1], sueldo_bruto, descuento_salud, descuento_afp, sueldo_liquido]
    trabajadores.append(trabajador)
    print("TRABAJADOR REGISTRADO CON ÉXITO!")
def opcion_2():
    if len(trabajadores)==0:
            print("No existen trabajadores, elija la opción 1")
    else:
        print("\tLISTA DE TRABAJADORES:")
        print("Tabajador\tCargo\tSueldo bruto\tDesc. Salud\tDesc. AFP\tLíquido a pagar")
        for t in trabajadores: #t es cada trabajador de la lista, t es una lista
            print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t{t[4]}\t\t{t[5]}")
def opcion_3():
    opc2=int(input("¿Qué cargo desea imprimir? (1:CEO, 2:DESARROLLADOR, 3:ANALISTA, 4:TODOS): "))
    if opc2==4:
        with open ("todos_trabajadores.txt", "w", newline="\n") as archivo:
            for t in trabajadores:
                texto=f"NOMBRE: {t[0]}\nCARGO: {t[1]}\nBRUTO: {t[2]}\nDESCTO SALUD: {t[3]}\nDESCTO AFP: {t[4]}\nLÍQUIDO: {t[5]}\n\n"
                archivo.write(texto)
    else:
        with open ("trabajadores_por_cargo.txt","w") as archivo:
            for t in trabajadores:
                if cargos[opc2-1]==t[1]:
                    texto=f"NOMBRE: {t[0]}\nCARGO: {t[1]}\nBRUTO: {t[2]}\nDESCTO SALUD: {t[3]}\nDESCTO AFP: {t[4]}\nLÍQUIDO: {t[5]}\n\n"
                    archivo.write(texto)
    print("Archivo creado con éxito!")
def opcion_4():
    print("Gracias por usar el programa, adios!")
    exit()