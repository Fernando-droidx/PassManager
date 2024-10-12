import tkinter as tk
from tkinter import messagebox as mg


class PassManager:
    def __init__(self):
        self.passwds = {}
    def agregar_pass(self, lista):

        def save_pass():
            name_account = box_acc_texto.get().strip()
            passwd = box_pass_texto.get().strip()
            if passwd != "":
                self.passwds[name_account] = passwd
                lista.insert(tk.END, name_account)
                mg.showinfo(title="Pass Original", message=f"Password: {passwd}")
                add_window.destroy()
            else:
                mg.showerror(title='Ingresa Texto', message='Tienes que ingresar texto para guardar')

        add_window = tk.Tk()
        add_window.title("Agregar nueva contraseña")
        add_window.geometry("300x150")

        etiqueta = tk.Label(add_window, text="Cuenta de usuario")
        etiqueta.pack()

        box_acc_texto = tk.Entry(add_window)
        box_acc_texto.pack()

        etiqueta = tk.Label(add_window, text="Contraseña de usuario")
        etiqueta.pack()

        box_pass_texto = tk.Entry(add_window, show="*")
        box_pass_texto.pack()

        save_button = tk.Button(add_window, text="Guardar la contraseña", command=save_pass)
        save_button.pack()


    def show(self, lista):
        selection = lista.curselection()  # Seleccionar el texto
        index = selection[0]
        name_account = lista.get(index)
        if not selection:
            mg.showerror("Error", "Selecciona una contraseña para verla")
        else:
            if name_account in self.passwds:
                passwd = self.passwds[name_account]
                mg.showinfo("Contraseña", f"La contraseña para '{name_account}' es: {passwd}")
            else:
                mg.showerror("Error", "La cuenta no tiene una contraseña asociada.")

    def eliminar_pass(self, lista):

        seleccion = lista.curselection()

        if seleccion:
            indice = seleccion[0]
            nombre_cuenta = lista.get(indice)
            del self.passwds[nombre_cuenta]
            lista.delete(indice)
            print(f"Cuenta '{nombre_cuenta}' eliminada.")
        else:
            mg.showerror("Error", "Selecciona una cuenta para eliminar")

    def actualizar_pass(self, lista):
        selection = lista.curselection()#Seleccionar el texto
        if not selection:
            mg.showerror("Error", "Selecciona una contraseña para actualizar")
        else:
            def save_pass():
                index = selection[0]
                lista.delete(index)
                var = update_box_texto.get()
                print(var)
                long = len(var)
                lista.insert(index, long*'*')
                mg.showinfo(title="Actulizacion", message="Actualizacion de la contrasena")
                add_window.destroy()

            add_window = tk.Tk()
            add_window.title("Actualizar contraseña")
            add_window.geometry("300x150")

            etiqueta = tk.Label(add_window, text="Ingresa una nueva contraseña")
            etiqueta.pack()

            update_box_texto = tk.Entry(add_window, show="*")
            update_box_texto.pack()

            update_button = tk.Button(add_window, text="Actualizar la contraseña", command=save_pass)
            update_button.pack()




