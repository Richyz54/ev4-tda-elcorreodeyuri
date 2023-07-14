import mysql.connector

class CConexion:
    
    def ConexionBaseDatos():
        try:
            conexion = mysql.connector.connect(user='admin',password='TDA123456.',host='yury.cjnplcvfcn4g.sa-east-1.rds.amazonaws.com',database='Yury',port='3306')
            print("Conexion exitosa.")

            return conexion

        except mysql.connector.Error as error:
            print("Error al conectarse a la base de Datos {}".format(error))

            return conexion
        




    ConexionBaseDatos()