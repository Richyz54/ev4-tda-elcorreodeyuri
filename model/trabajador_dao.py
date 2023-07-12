from conexion_db import ConexionDB

def logQuery():
    
    a=" ******************************\n"
    b="*      QUERY FINALIZADA      *\n"
    c="******************************\n"
    print(a,b,c)

def listar():
    conexion = ConexionDB()
    listado_trabajadores = []
    sql = "SELECT * FROM Trabajadores;"
    try:
        cursor=conexion.cursor.execute(sql)   
        print("EJECUTA QUERY SELECT \n")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()
        
def insertar():
    conexion = ConexionDB()
    sql = "Insert into Trabajadores(RutTrabajador, Nombre, SexoTrabajador, CargoTrabajador, FechaIngreso, Area, Departamento, Direccion, TelefonoTrabajador) VALUES('2222-9','ADMIN2','NA','NA','2023/07/11','RRHH','RRHH','Coyancura 2288','987654321');"
    try:
        conexion.cursor.execute(sql)   
        print("EJECUTA QUERY INSERT \n")
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()

        
def eliminar():
    conexion = ConexionDB()
    sql = "delete from Trabajadores where RutTrabajador = '2222-9';"
    try:
        conexion.cursor.execute(sql)   
        print("EJECUTA QUERY ELIMINAR \n")
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        conexion.cerrar()
        logQuery()

    
# listar()
# insertar()
# listar()
# eliminar()
# listar()


