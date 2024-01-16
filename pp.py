
from BD.conexion import DAO #permite conectar archivos en el directorio DB el archivo conecxion 
import funciones # importamos el archivo funciones
#from conecdb import *

def menuPrincipal():
    continuar=True
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print ("========MENU PRINCIPAL======")
            print ("1.- Ver leer la luz")
            print ("2.- Escribir datos electrico")
            print ("3.- Ver tabla Dispositivos")
            print ("4.- Ver tabla Inmuebles")
            print ("5.- Ver tabla Modelos")
            print ("6.- Ver tabla Variables")
            print ("7.- =======Salir==================")
            opcion = int(input("Selecione una opcion: "))

            if opcion < 1 or opcion > 7:
                print("opcion incorrecta, ingrese nuevamente...")
            elif opcion == 7:
                continuar = False
                print ("gracias por su tiempo")
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()
    
    if opcion == 1:
        try:
            elementos = dao.listarElementos()
            if len(elementos) > 0:
                print("elementos largo",len(elementos))
                funciones.listarElementos(elementos)
            else :
                print("No se encontraton Elemetos")
        except:
            print("ocurrio un error..aqui...")

    elif opcion == 2:
        try:
            print("Opcion 2")
            dtelect = funciones.get_data_http('192.168.100.33','0')
            print('Elect=',dtelect)
            print(dtelect['apower'])
            print(dtelect['voltage'])
            print(dtelect['current'])
            print("aenery",dtelect['aenergy']['total'])
            print("byminute",dtelect['aenergy']['by_minute'][0])
            print("minute_ts",dtelect['aenergy']['minute_ts'])
            print("temperoatue",dtelect['temperature']['tC'])
            dao.registrarDato(dtelect)
            # elementos = dao.mostrartabla()
           # funciones.listarTabla(elementos)
        except:
            print("Ocurrio un error.opcio2...")
    elif opcion ==3:
        print("Opcion 3")
        equi = dao.equipo('192.168.100.33')
        print(equi)
        print(len(equi))
        print(type(equi))
        #print(equi[-1])
        print(equi[0])
    elif opcion ==4:
        print("Opcion 4")
    else:
        print("Opcion no valida....")


menuPrincipal() 
    