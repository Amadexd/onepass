import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = '192.168.100.47',
        port=3306,
        user='root',
        password='k1munsp4',
        db='smmce_python'
    )
    
    if conexion.is_connected( ):
        print("Conexxion existosa")
        inforServer = conexion.get_server_info()
        print ("informacion del Server :", inforServer) 
except Error as ex:
    print ("Error durante la conexion : ", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("la conección se ha cerrado")
