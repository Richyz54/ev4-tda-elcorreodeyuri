from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pyodbc

#abre una ventana que contendra el login
root=Tk()
root.title("Login")
root.geometry("500x300")
root.resizable(width=False, height=False)

usuario = Label(root, text="RutTabajador")
usuario.pack()
usuario1 = StringVar()
usu=Entry(root, width=30, textvariable=usuario1)
usu.pack()

contraseña = Label(root, text="Contraseña")
contraseña.pack()

contra= StringVar()
contra1=Entry(root, width=30, textvariable=contra, show="*")
contra1.pack()

# abre una conexion con la base de datos valida el rut y la contraseña del usuario, trae el tipo de usuario y abre menu distinto segun el tipo de usuario.
def validar():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=sqlserver.cjnplcvfcn4g.sa-east-1.rds.amazonaws.com;DATABASE=Yury;UID=admin;PWD=TDA123456.')
        cursor = connection.cursor()
        cursor.execute("SELECT TipoUsuario FROM UsuarioSistema WHERE RutTrabajador='"+usuario1.get()+"' and Contraseña='"+contra.get()+"'")
        
        if cursor.fetchval():
            messagebox.showinfo("Inicio secion Exitoso","Inicio secion Exitoso")
            cursor.execute("SELECT TipoUsuario FROM UsuarioSistema WHERE RutTrabajador='"+usuario1.get()+"' and Contraseña='"+contra.get()+"'")
            TipoUsuario  = cursor.fetchval()
            connection.close()
            if TipoUsuario == "Admin":
                messagebox.showinfo("pagina inicio","Bienvenido Admin")
                root.withdraw()
                from menuListado import main
                main()
            elif TipoUsuario == "RRHH":
                messagebox.showinfo("pagina inicio","Bienvenido RRHH")
                root.withdraw()
                from menuRRHH import main
                main()
            elif TipoUsuario == "Trabajador":
                messagebox.showinfo("pagina inicio","Bienvenido Trabajador")
                root.withdraw()

        else:
            messagebox.showwarning("Inicio secion fallido","Rut o contraseña Incorrecto")

    except Exception as ex:
        messagebox.showerror("Error en la BD","Error durante la conexión: {}".format(ex))
    finally:
        connection.close()

#boton que ejecuta la accion de validar
Button (root, text="Iniciar Sesion", width=30, command = validar).pack()


root.mainloop()
