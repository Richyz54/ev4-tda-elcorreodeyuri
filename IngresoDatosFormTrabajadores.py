from Conexion import *

class IngresoTrabajador:

    def mostrarTrabajadores():
        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            cursor.execute("select * from Trabajadores;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error de despliegue de datos: {}".format(error))



    def ingresarTrabajador(rut,nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono):

        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql ="insert into Trabajadores values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla
            #Como minima expresion es: (valor,) la coma hace que sea una tupla
            valores = (rut,nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))



    def modificarTrabajador(rut,nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono):

        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql ="update Trabajadores SET Trabajadores.Nombre = %s,Trabajadores.SexoTrabajador = %s,Trabajadores.CargoTrabajador = %s,Trabajadores.FechaIngreso = %s,Trabajadores.Area = %s,Trabajadores.Departamento = %s,Trabajadores.Direccion = %s,Trabajadores.TelefonoTrabajador = %s where Trabajadores.RutTrabajador =%s;"
            valores = (nombre,sexo,cargo,fehaingreso,area,departamento,direccion,telefono,rut)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de actualización de datos: {}".format(error))


    def eliminarTrabajador(rut):

        try:
            cone = CConexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql ="delete from Trabajadores where Trabajadores.RutTrabajador = %s;"
            valores = (rut,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de eliminacion de datos: {}".format(error))