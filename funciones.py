import csv
import os
def abrir_archivo(nombre_archivo):
    try:
        open(nombre_archivo)
    except IOError:
        return False
    return True

def modificar(nombre_archivo, modo):
    with open(nombre_archivo, modo, newline='') as f_nomina:
        csv_nomina = csv.writer(f_nomina, delimiter=";")
        
        if modo == 'w':
            cabecera = "Legajo", "Apellido", "Nombre"
            csv_nomina.writerow(cabecera)
        
        seguir = "1"
        while seguir == "1":

            in_legajo = input("Ingrese el legajo: ")
        
            while in_legajo.isdecimal() == False:
                in_legajo = input("Legajo inválido, ingreselo nuevamente: ")
            
            in_apellido = input("Ingrese apellido: ")
            in_nombre = input("Ingrese nombre: ")
            fila = in_legajo, in_apellido, in_nombre
            csv_nomina.writerow(fila)
            seguir = input("Dese seguir cargando? 1- si 2- no\n")


def crear(nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as f_nomina:    
        csv_nomina = csv.writer(f_nomina)
        cabecera = "Legajo","Apellido","Nombre"
        csv_nomina.writerow(cabecera)
    print("Archivo creado con exito en ", os.path.abspath(nombre_archivo))

def viaticos(nombre_archivo, legajo):
    limite = 5000
    viaticos = 0
    with open(nombre_archivo, 'r') as f_nomina:
        with open('viaticos.csv', 'r') as f_viaticos:
            csv_nomina = csv.reader(f_nomina, delimiter=";")
            csv_viaticos = csv.reader(f_viaticos, delimiter=";")
            next(csv_nomina)
            
            contador = 0
            
            for viatico in csv_viaticos:
                contador += 1

                if viatico[0] == legajo:
                    viaticos += float(viatico[1])

            for empleado in csv_nomina:
                if empleado[0] == legajo:
                    nombre = empleado[2]
                    apellido = empleado[1]
            
        try:       
            if viaticos > 5000:
                print(f"Legajo {legajo}: {nombre} {apellido}, gastó ${viaticos} y se ha pasado del presupuesto por: ${viaticos - limite}.")
            else:
                print(f"Legajo {legajo}: {nombre} {apellido}, gastó ${viaticos}.")

        except UnboundLocalError:
            print(f"No se encontró el Legajo: {legajo}")