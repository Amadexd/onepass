import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = '192.168.100.x',
        port=3306,
        user='root',
        password='k1munsp4',
        db='smmce_python'
    )
    
    if conexion.is_connected( ):
        print("Conexxion existosa")
        cursor=conexion.cursor()
        cursor.execute("SELECT database();")
        registro=cursor.fetchone()
        print("Conectado a la base de datos", registro)
        cursor.execute("SELECT * FROM circuitos")
        resultados=cursor.fetchall()
        print("columnas", cursor.column_names)
        print("largo de columnas de tablas",len(cursor.column_names))
        for fila in resultados:
            print(fila[0],fila[1],fila[2])
        print("Total de Filas o registros", cursor.rowcount)
       

except Error as ex:
    print ("Error durante la conexion : ", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("la conección se ha cerrado")
