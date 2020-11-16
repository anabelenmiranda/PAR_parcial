'''
El programa deberá correr sin errores de ejecución.
Se evaluará el programa de manera integral: el orden del código, 
documentación, modularidad, manejo de errores y excepciones,  etc. 
Tiene máximo 3hs para resolverlo, probarlo y subir a un repositorio 
de github de su propiedad,  y pasar vía mensaje privado al Slack el 
link o bien el link por email. Se requiere al menos 2 commits para 
mostrar el progreso de su trabajo.
Los mensajes/emails recibidos luego de las 22hs del lunes 16 de 
noviembre no serán tenidos en consideración y quedará reprobado 
automáticamente, teniendo que recursar el año siguiente.

Todos los ejercicios deberán contener las validaciones y excepciones 
correspondientes.
'''

# Usted ha sido contratado para desarrollar una solución que le permita 
# al dpto. De RRHH obtener de manera ágil el estado de los gastos por 
# viáticos. 

# La empresa tiene los datos de viáticos del mes en un archivo csv. 
# El sistema deberá :
# Tener un menú de acciones 
# Permitir la carga de datos del legajo completo (legajo, apellido, nombre)
# y guardarlos en un archivo csv cuyo nombre será dado por el usuario. 
# Si el archivo ya existe deberá preguntar si se desea agregar o 
# sobreescribirlo. * sólo validar que Legajo  sea un entero
# Dado el número de legajo de un empleado calcular e informar en 
# pantalla los gastos que hizo hasta el momento,  junto con el resto 
# de sus datos. Si superó los $5000 indicar que se ha pasado del 
# presupuesto y por cuanto. Por ejemplo "Legajo 1 : Laura Estebanez, 
# gastó $9000 y se ha pasado del presupuesto por $4000" 
# Caso contrario solo mostrar:  "Legajo 1 : Laura Estebanez, gastó $488" 

# Tenga en cuenta que las acciones del menú no tienen un orden en particular.

import funciones
def menu():
    while True:
        opcion = input("*** MENU ***\n1- Crear o cargar archivo\n2- Consultar gastos\n3- Salir\n")
        
        if opcion == "1":
            nombre_archivo = input("Ingrese nombre de archivo: ")
            if funciones.abrir_archivo(nombre_archivo) == False:
                ingreso = input("El archivo no existe!\nDesea crear uno nuevo? 1 - 'si' / 2 - 'no'")
                
                if ingreso == "1":
                    funciones.crear(nombre_archivo)
                    print("Creado!")
                    pass
                elif ingreso == "2":
                    print("El archivo no se ha creado")
                    pass
                else:
                    print("Ingreso incorrecto")
                    pass
            else:
                modificar = input("1- Sobreescribir / 2- Cargar datos")
                if modificar == "1":
                    funciones.modificar(nombre_archivo, "w")
                elif modificar == "2":
                    funciones.modificar(nombre_archivo, "a")
        elif opcion == "2":
            nombre_archivo = input("Ingrese nombre de archivo: ")
            if funciones.abrir_archivo(nombre_archivo) == False:
                ingreso = input("El archivo no existe!\nDesea crear uno nuevo? 1 - 'si' / 2 - 'no'")
                
                if ingreso == "1":
                    funciones.crear(nombre_archivo)
                    print("Creado!")
                elif ingreso == "2":
                    print("no se ha creado")
                    pass
                else:
                    print("Ingreso incorrecto")
                    pass
            else:
                legajo = ""
                while legajo.isdecimal() == False:
                    legajo = input("Ingrese legajo a buscar: ")
                funciones.viaticos(nombre_archivo, legajo)
                pass
        elif opcion == "3":
            exit()
menu()