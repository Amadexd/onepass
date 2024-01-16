from BD.conexion import DAO
import funciones 

def menuPrincipal():
    continuar=True
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print ("========MENU PRINCIPAL======")
            print ("1.- Ver tabla Marcas")
            print ("2.- Ver tabla Circuitos")
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

    elif opcion ==2:
        try:
            print("Opcion 2")
            elementos = dao.mostrartabla()
            funciones.listarTabla(elementos)
        except:
            print("Ocurrio un error....")
    elif opcion ==3:
        print("Opcion 3")
    elif opcion ==4:
        print("Opcion 4")
    else:
        print("Opcion no valida....")

menuPrincipal() 
    