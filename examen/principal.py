import funciones as fn

trabajadores = [
    "Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez",
        "Pedro Rodriguez","Laura Hernandez","Miguel Sanchez",
        "Isabel Gomez","Francisco Diaz","Elena Fernandez"
            ]

lista_sueldos = {}

while True:
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    opcion=int(input("Ingrese una opción: "))

    if opcion == 1:
        print("Lista de sueldos")
        print("*****************")
        lista_sueldos = fn.sueldos_aleatorios(trabajadores)
        print("*****************")

    elif opcion == 2:
        fn.clasificar_sueldos(lista_sueldos)
     
    else:
        opcion == 5
        print("Finalizando programa...")
        print("Desarrollado por Diego Hernandez")
        print("RUT 21.620.968.0")
        break

         

    
            