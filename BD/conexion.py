import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host = 'localhost',
                port=3306,
                user='sgeme',
                password='simon2620',
                database='dtelec'
            )
        except Error as ex:
            print("Error al intertar la conexión: {0}".format(ex))

    def listarElementos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM datos_elect ORDER BY id ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intertar la conexión: {0}".format(ex))
    
    def mostrartabla(self):
         if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM circuitos ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intertar la conexión: {0}".format(ex))

    def registrarDato(self, dtelect):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                #sql = "INSERT INTO datos_elect (corr, volt, pot, tiempo) VALUES ('{0}', '{1}', '{2}', '{3}')"
                #cursor.execute(sql.format(dtelect['current'],dtelect['voltage'], dtelect['apower'], dtelect['minute_ts']))
                sql = "INSERT INTO datos_elect (corr, volt, pot, tiempo, temp, id_eq) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')"
                cursor.execute(sql.format(dtelect['current'],dtelect['voltage'], dtelect['apower'], dtelect['aenergy']['minute_ts'],dtelect['temperature']['tC']),dtelect['id_eq'])
                print(sql)
                self.conexion.commit()
                print("¡Curso registrado opcion 2!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    def equipo(self, ip):
         if self.conexion.is_connected():
            try:
                nombre_var = ['ideq', 'modelo', 'url', 'ip', 'sw_id']
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM equipos WHERE ip = '{0}'"
                cursor.execute(sql.format(ip))
                resultados = cursor.fetchall()
                print("en funcion0",resultados[0])
                nombre_datos_eq = dict(zip(nombre_var,resultados[0]))
                print("en funcion",nombre_datos_eq)
                return nombre_datos_eq
            except Error as ex:
                print("Error al intertar la conexión: {0}".format(ex))

    def id_equipo(self,ip,idsw):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT id FROM equipos WHERE ip = '{0}' and tipo_sw = '{1}'"
                cursor.execute(sql.format(ip,idsw))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intertar la conexión: {0}".format(ex))