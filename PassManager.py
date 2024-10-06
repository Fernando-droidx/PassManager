import tkinter as tk
from tkinter import messagebox as mg

class PassManager:
    def __init__(self):
        self.passwds = []
    def agregar_pass(self, lista):
        def save_pass():
            passwd = box_texto.get().strip()
            long = len(passwd)
            if passwd != "":
                self.passwds.append(passwd)
                lista.insert(tk.END, long*'*')
                print(passwd)
                add_window.destroy()
            else:
                mg.showerror(title='Ingresa Texto', message='Tienes que ingresar texto para guardar')

        add_window = tk.Tk()
        add_window.title("Agregar nueva contraseña")
        add_window.geometry("300x150")

        etiqueta = tk.Label(add_window, text="Ingresa una nueva contraseña")
        etiqueta.pack()

        box_texto = tk.Entry(add_window, show="*")
        box_texto.pack()

        save_button = tk.Button(add_window, text="Guardar la contraseña", command=save_pass)
        save_button.pack()

    def eliminar_pass(self, lista):
        selection = lista.curselection()
        if selection:
            lista.delete(selection)
            mg.showinfo(title="Eliminada", message="Eliminado")
        else:
            mg.showerror("Error", "Selecciona una contraseña para eliminar")

    def actualizar_pass(self, lista):
        selection = lista.curselection()#Seleccionar el texto
        if not selection:
            mg.showerror("Error", "Selecciona una contraseña para actualizar")
        else:
            def save_pass():
                index = selection[0]
                lista.delete(index)
                var = update_box_texto.get()
                long = len(var)
                lista.insert(index, long*'*')
                mg.showinfo(title="Actulizacion", message="Actualizacion de la contrasena")

            add_window = tk.Tk()
            add_window.title("Actualizar contraseña")
            add_window.geometry("300x150")

            etiqueta = tk.Label(add_window, text="Ingresa una nueva contraseña")
            etiqueta.pack()

            update_box_texto = tk.Entry(add_window, show="*")
            update_box_texto.pack()

            update_button = tk.Button(add_window, text="Actualizar la contraseña", command=save_pass)
            update_button.pack()


