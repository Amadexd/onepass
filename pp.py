
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
            print ("5.- Ver tabla Equipos")
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
            #print('Elect=',dtelect)
            ''' 
            print(dtelect['apower'])
            print(dtelect['voltage'])
            print(dtelect['current'])
            print("aenery",dtelect['aenergy']['total'])
            print("byminute",dtelect['aenergy']['by_minute'][0])
            print("minute_ts",dtelect['aenergy']['minute_ts'])
            print("temperoatue",dtelect['temperature']['tC'])
            '''  
            equi = dao.id_equipo('192.168.100.30',0)
            print("equi",equi)
            '''
            if isinstance(equi[0], str):
                print("equi0", int(equi[0]))
            else:
                print("El primer elemento no es una cadena y no se puede convertir a entero.")
            '''
            print("equi00",int(equi[0][0]))

            #print(type(equi))
            #entero_primer = int(equi[0])
            #print("imprimiendo",entero_primer)
            #print("longitud ",len(equi))
            #enter = 0 
            #enter = enter + [int(equi[0])]
            #print("equio en cuadrado",enter)
            dtelect['id_eq'] = int(equi[0][0])
            print("equi en opcion2",dtelect)
            
            #dao.registrarDato(dtelect)
            # elementos = dao.mostrartabla()
           # funciones.listarTabla(elementos)
          
        except:
            print("Ocurrio un error.opcio2...")
    elif opcion ==3:
        print("Opcion 3")
        #nombre_var = ['ideq', 'modelo', 'url', 'ip', 'sw_id']
        equi = dao.equipo('192.168.100.33')
        print("pp",equi['ip'],equi['url'],equi['sw_id'],)

    elif opcion ==4:
        print("Opcion 4")
        equi = dao.id_equipo('192.168.100.30',0)
        print(equi)
    else:
        print("Opcion no valida....")


menuPrincipal() 
    