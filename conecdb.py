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

    def listaElementos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM datos_elect ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intertar la conexión: {0}".format(ex))

    def registrarDato(self, dtelect):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO datos_elect (corr, volt, pot) VALUES ('{0}', '{1}', {2})"
                cursor.execute(sql.format(dtelect[0], dtelect[1], dtelect[2]))
                print(sql)
                self.conexion.commit()
                print("¡Curso registrado opcion 2!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
