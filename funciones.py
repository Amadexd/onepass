import requests

def listarElementos(elementos):
    print("DAtos")
    contador = 1
    for cur in elementos:
        datos = "{0}. Datos1: {1} | Datos2: {2} ({3} datos3)"
        print(datos.format(contador, cur[0],cur[1],cur[2]))
        contador = contador + 1 
    print("   ")

def listarTabla(dato):
    print("Tabla XXXXXX")
    contador = 1
    for cur in dato:
        datos = "{0} | {1} |  {2} | {3} | {4})"
        print(datos.format(contador, cur[0],cur[1],cur[2],cur[4]))
        contador = contador + 1 
    print("   ")

### INFORMACION DE LOS DISPOSITIVOS
#def information_device(database):
#    device = Devices()
#
#    for arr in database.lectura_device():
#        if arr[4] == 'Modbus TCP':
#            reg = database.lectura_modbusTCP()
#            d = Device(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6],
#                       unitId=reg[0], address=reg[1], quantity=reg[2], typeData=reg[3])
#        elif arr[4] == 'HTTP':
#            reg = database.lectura_http(arr[0], arr[3])
#            d = Device(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], switch=reg)
#            
#        device.add_device(d)
#
#    return device.get_devices()
###
# LECTURA DE DATOS POR HTTP REQUESTS
def get_data_http(ip: str, switch: str):
#    url = 'http://' + ip + config('METHOD_URL') + switch
    
    url = 'http://' + ip + '/rpc/Switch.GetStatus?id=' + switch
    # print(url)
    data = requests.get(url).json()
    # print(data)
    return data
#    print(data)
    # Datos para enviar por HTTP request
#    values = { 'salida': str(data['output']), 'voltaje': data['apower'],
#              'corriente': data['current'], 'potencia': data['apower'],
#              'energia': ((data['aenergy']['total'])/1000), 'pf': data['pf'],
#              'temperatura': data['temperature']['tC'] }

#    # Datos para enviar a la base de datos
#    valuesDb = [data['voltage'], data['current'], data['apower'],
#                ((data['aenergy']['total'])/1000), data['pf'],
#
#                 data['temperature']['tC'], data['temperature']['tF']]
#return
#return values    
#    return values, valuesDb