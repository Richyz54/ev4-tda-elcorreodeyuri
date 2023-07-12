import tkinter as tk
from client.gui_app import Frame, barra_menu
def main():
    root = tk.Tk()
    root.title('Empresa: El correo de Yuri')
    root.iconbitmap('img/Lupa.ico')
    root.resizable(0,0)      #Cambia el tamaño de la ventana
    barra_menu(root)

    app = Frame(root = root)

    app.mainloop()

if __name__ == '__main__':
    main()  