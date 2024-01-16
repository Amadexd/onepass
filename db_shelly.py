import mysql.connector
from mysql.connector import Error
from decouple import config

class Mysql():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = '192.168.100.102',
                port=3306,
                user='sgeme',
                password='simon2620',
                database='dtelec'
                )
            # Crea un cursor para realizar una sentencia SQL
            self.cursor = self.connection.cursor()

            print('Conexión realizada con éxito.')
            
        except Error as ex:
            ('Se ha producido un error en la conexión: ', ex)
        
    # Entrega la informacion de todos los dispositivos desde la tabla 'devices' en la base de datos
"""
    def lectura_device(self):
        self.cursor.execute('''
        SELECT
	        modelos.nombre,
	        dispositivos.ip,
	        inmuebles.nombre,
	        circuitos.nombre,
	        dispositivos.conexion,
            dispositivos.modelo_id,
            dispositivos.id
        FROM
	        dispositivos
        INNER JOIN modelos ON modelos.id = dispositivos.modelo_id
        INNER JOIN inmuebles ON inmuebles.id = dispositivos.inmueble_id
        INNER JOIN circuitos ON circuitos.id = dispositivos.circuito_id
        ''')
        resultados = self.cursor.fetchall()
        return resultados

    # Entrega los parametros de conexion Modbus TCP de un dispositivo desde la base de datos al sistema
    def lectura_modbusTCP(self):
        ads, qua, typ = [], [], []
        self.cursor.execute('''
        SELECT
            dispositivos.unit_id,
            registros.address,
            registros.quantity,
            registros.type_data
        FROM
            modelos
        INNER JOIN registros ON registros.modelo_id = modelos.id
        INNER JOIN dispositivos ON dispositivos.modelo_id = modelos.id
        ''')
        resultados = self.cursor.fetchall()
        for result in resultados:
            ads.append( result[1] )     # Address
            qua.append( result[2] )     # Quantity
            typ.append( result[3] )     # Type Data
        return [resultados[0][0], ads, qua, typ]

    # Entrega los parametros de conexion HTTP de un dispositivo desde la base de datos al sistema
    def lectura_http(self, nombre, circuito):
        sentencia = '''
        SELECT
        	dispositivos.switch
        FROM
        	dispositivos
        INNER JOIN modelos ON modelos.nombre = '{0}' AND dispositivos.modelo_id = modelos.id
        INNER JOIN circuitos ON circuitos.nombre = '{1}' AND dispositivos.circuito_id = circuitos.id
        '''.format(nombre, circuito)
        self.cursor.execute(sentencia)
        resultado = self.cursor.fetchall()
        return resultado[0][0]

    # Agrega las mediciones del Powys 1110 a la base de datos
    def agregar_powys1110(self, arr, id):
        try:
            sentencia = '''
            INSERT INTO
                valores(valor, variable_id, dispositivo_id)
            VALUES
                ({1}, (SELECT id FROM variables WHERE nombre = 'Voltaje'), {0}),
                ({2}, (SELECT id FROM variables WHERE nombre = 'Corriente'), {0}),
                ({3}, (SELECT id FROM variables WHERE nombre = 'Potencia Activa'), {0}),
                ({4}, (SELECT id FROM variables WHERE nombre = 'Energia Activa'), {0}),
                ({5}, (SELECT id FROM variables WHERE nombre = 'pf'), {0}),
                ({6}, (SELECT id FROM variables WHERE nombre = 'cosphi'), {0}),
                ({7}, (SELECT id FROM variables WHERE nombre = 'Frecuencia'), {0}),
                ({8}, (SELECT id FROM variables WHERE nombre = 'Potencia Reactiva'), {0}),
                ({9}, (SELECT id FROM variables WHERE nombre = 'Potencia Aparente'), {0}),
                ({10}, (SELECT id FROM variables WHERE nombre = 'THDV'), {0}),
                ({11}, (SELECT id FROM variables WHERE nombre = 'THDI'), {0}),
                ({12}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 1'), {0}),
                ({13}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 3'), {0}),
                ({14}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 5'), {0}),
                ({15}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 7'), {0}),
                ({16}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 9'), {0}),
                ({17}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 11'), {0}),
                ({18}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 13'), {0}),
                ({19}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 15'), {0}),
                ({20}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 17'), {0}),
                ({21}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 19'), {0}),
                ({22}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 21'), {0}),
                ({23}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 23'), {0}),
                ({24}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 25'), {0}),
                ({25}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 27'), {0}),
                ({26}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 29'), {0}),
                ({27}, (SELECT id FROM variables WHERE nombre = 'Armonico de Voltaje 31'), {0}),
                ({28}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 1'), {0}),
                ({29}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 3'), {0}),
                ({30}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 5'), {0}),
                ({31}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 7'), {0}),
                ({32}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 9'), {0}),
                ({33}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 11'), {0}),
                ({34}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 13'), {0}),
                ({35}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 15'), {0}),
                ({36}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 17'), {0}),
                ({37}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 19'), {0}),
                ({38}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 21'), {0}),
                ({39}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 23'), {0}),
                ({40}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 25'), {0}),
                ({41}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 27'), {0}),
                ({42}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 29'), {0}),
                ({43}, (SELECT id FROM variables WHERE nombre = 'Armonico de Corriente 31'), {0}),
                ({44}, (SELECT id FROM variables WHERE nombre = 'Voltaje max'), {0}),
                ({45}, (SELECT id FROM variables WHERE nombre = 'Corriente max'), {0}),
                ({46}, (SELECT id FROM variables WHERE nombre = 'Frecuencia max'), {0}),
                ({47}, (SELECT id FROM variables WHERE nombre = 'cosphi max'), {0}),
                ({48}, (SELECT id FROM variables WHERE nombre = 'pf max'), {0}),
                ({49}, (SELECT id FROM variables WHERE nombre = 'Potencia Activa max'), {0}),
                ({50}, (SELECT id FROM variables WHERE nombre = 'Potencia Reactiva max'), {0}),
                ({51}, (SELECT id FROM variables WHERE nombre = 'Potencia Aparente max'), {0}),
                ({52}, (SELECT id FROM variables WHERE nombre = 'THDV max'), {0}),
                ({53}, (SELECT id FROM variables WHERE nombre = 'THDI max'), {0}),
                ({54}, (SELECT id FROM variables WHERE nombre = 'Voltaje min'), {0}),
                ({55}, (SELECT id FROM variables WHERE nombre = 'Corriente min'), {0}),
                ({56}, (SELECT id FROM variables WHERE nombre = 'Frecuencia min'), {0}),
                ({57}, (SELECT id FROM variables WHERE nombre = 'cosphi min'), {0}),
                ({58}, (SELECT id FROM variables WHERE nombre = 'pf min'), {0}),
                ({59}, (SELECT id FROM variables WHERE nombre = 'Potencia Activa min'), {0}),
                ({60}, (SELECT id FROM variables WHERE nombre = 'Potencia Reactiva min'), {0}),
                ({61}, (SELECT id FROM variables WHERE nombre = 'Potencia Aparente min'), {0}),
                ({62}, (SELECT id FROM variables WHERE nombre = 'THDV min'), {0}),
                ({63}, (SELECT id FROM variables WHERE nombre = 'THDI min'), {0}),
                ({64}, (SELECT id FROM variables WHERE nombre = 'Demanda Corriente'), {0}),
                ({65}, (SELECT id FROM variables WHERE nombre = 'Demanda Potencia Activa'), {0}),
                ({66}, (SELECT id FROM variables WHERE nombre = 'Demanda Potencia Reactiva'), {0}),
                ({67}, (SELECT id FROM variables WHERE nombre = 'Demanda Potencia Aparente'), {0}),
                ({68}, (SELECT id FROM variables WHERE nombre = 'Medidor hora funcionando'), {0}),
                ({69}, (SELECT id FROM variables WHERE nombre = 'Medidor hora encendido'), {0}),
                ({70}, (SELECT id FROM variables WHERE nombre = 'Medidor interrupcion de potencia'), {0}),
                ({71}, (SELECT id FROM variables WHERE nombre = 'Exportar Energia Activa'), {0}),
                ({72}, (SELECT id FROM variables WHERE nombre = 'Importar Energia Reactiva'), {0}),
                ({73}, (SELECT id FROM variables WHERE nombre = 'Exportar Energia Reactiva'), {0});
            '''.format(id, arr[0], arr[1], arr[5], arr[69], arr[4], arr[3], arr[2], arr[6], arr[7],
            arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], arr[15], arr[16], arr[17],
            arr[18], arr[19], arr[20], arr[21], arr[22], arr[23], arr[24], arr[25], arr[26], arr[27],
            arr[28], arr[29], arr[30], arr[31], arr[32], arr[33], arr[34], arr[35], arr[36], arr[37],
            arr[38], arr[39], arr[40], arr[41], arr[42], arr[43], arr[44], arr[45], arr[46], arr[47],
            arr[48], arr[49], arr[50], arr[51], arr[52], arr[53], arr[54], arr[55], arr[56], arr[57],
            arr[58], arr[59], arr[60], arr[61], arr[62], arr[63], arr[64], arr[65], arr[66], arr[67],
            arr[68], arr[70], arr[71], arr[72])
            self.cursor.execute(sentencia)
            self.connection.commit()
        except Error as ex:
            print('Error al almacenar las mediciones: ', ex)

    # Agrega las mediciones de los Shelly Pro a la base de datos
    """
    def agregar_shelly(self, arr, id):
        try:
            sentencia = '''
            INSERT INTO
                valores(valor, variable_id, dispositivo_id)
            VALUES
                ({1}, (SELECT id FROM variables WHERE nombre = 'Voltaje'), {0}),
                ({2}, (SELECT id FROM variables WHERE nombre = 'Corriente'), {0}),
                ({3}, (SELECT id FROM variables WHERE nombre = 'Potencia Activa'), {0}),
                ({4}, (SELECT id FROM variables WHERE nombre = 'Energia Activa'), {0}),
                ({5}, (SELECT id FROM variables WHERE nombre = 'pf'), {0}),
                ({6}, (SELECT id FROM variables WHERE nombre = 'Temperatura C'), {0}),
                ({7}, (SELECT id FROM variables WHERE nombre = 'Temperatura F'), {0});
            '''.format(id, arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])
            self.cursor.execute(sentencia)
            self.connection.commit()
        except Error as ex:
            print('Error al almacenar las mediciones: ', ex)

    # Cierra la comunicación con la base de datos
    def cerrar(self):
        self.cursor.close()
        self.connection.close()
        print('La conexión ha finalizado.')