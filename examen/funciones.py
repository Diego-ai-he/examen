import random
import csv



def sueldos_aleatorios(trabajadores):

    lista_sueldos = {}

    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        

        lista_sueldos[trabajador] = sueldo

    print(lista_sueldos)
    return lista_sueldos

    
def clasificar_sueldos(lista_sueldos):
        menor_800000 = {}
        mayor2000000 = {}
        entre800_2000000 = {}

        for trabajador in lista_sueldos.items():
            if sueldo < 800000:
                menor_800000[lista_sueldos] = sueldo
            elif sueldo <= 1500000:
                entre800_2000000[lista_sueldos] = sueldo
            else:
                mayor2000000[lista_sueldos] = sueldo

    
        
    
    #mostrar la clasifi
        print("Sueldos menores a 800 TOTAL:",len(menor_800000))
        for trabajador,sueldo in menor_800000:
         print(trabajador,":  $",sueldo)
        
        

        print("Sueldos entre 800.000 y 2.000.000 TOTAL:",len(entre800_2000000))
        for trabajador,sueldo in entre800_2000000:
            print(trabajador,":  $",sueldo)
            

        print("Sueldos mayores a 2.000.000 TOTAL:",len(mayor2000000))
        for trabajador,sueldo in mayor2000000:
            print(trabajador,":  $",sueldo)
            
 