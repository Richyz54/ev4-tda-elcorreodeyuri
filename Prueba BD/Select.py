import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=sqlserver.cjnplcvfcn4g.sa-east-1.rds.amazonaws.com;DATABASE=Yury;UID=admin;PWD=TDA123456.')
    print("Conexión exitosa.")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Trabajadores")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()
    print("La conexión ha finalizado.")