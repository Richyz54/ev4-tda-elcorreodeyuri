import tkinter as tk
from client.gui_app import Frame, barra_menu
def main():
    root = tk.Tk()
    
    #Ventana de interfaz de salida
    root.title('EL CORREO DE YURI')
    root.iconbitmap('img/logo.ico')
    #root.resizable(0,0)      #Cambia el tamaño de la ventana
    barra_menu(root)

    app = Frame(root = root)

    #Fin de ejecución
    app.mainloop()

if __name__ == '__main__':
    main()  