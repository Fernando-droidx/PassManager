import tkinter as tk
from tkinter import messagebox as mg


class PassManager:
    def __init__(self):
        self.passwds = {}
    def pass_verification(self, passwd):
        if len(passwd) < 7:
            mg.showerror(title='Longitud', message='La contrasena no es suficiente de 8 caracteres')
            return False
        return True
    def agregar_pass(self, lista):

        def save_pass():
            name_account = box_acc_texto.get().strip()
            passwd = box_pass_texto.get().strip()
            if not self.pass_verification(passwd):
                add_window.destroy()
                return "Contrasena incorrecta"


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
                lista.delete(index)#borramos el elemento seleccionado
                var_pass = update_passwd_box_texto.get()
                var_acoun = update_acc_box_texto.get()
                if not self.pass_verification(var_pass):
                    add_window.destroy()
                    return "Contrasena incorrecta"

                if var_pass != "":
                    self.passwds[var_acoun] = var_pass
                    lista.insert(tk.END, var_acoun)
                    mg.showinfo(title="Update Password", message=f"Password: {var_pass}")
                    add_window.destroy()
                else:
                    mg.showerror(title='Ingresa Texto', message='Tienes que ingresar texto para guardar')

            add_window = tk.Tk()
            add_window.title("Actualizar contraseña")
            add_window.geometry("300x150")

            etiqueta = tk.Label(add_window, text="Cuenta de usuario")
            etiqueta.pack()

            update_acc_box_texto = tk.Entry(add_window)
            update_acc_box_texto.pack()

            etiqueta = tk.Label(add_window, text="Contraseña de usuario")
            etiqueta.pack()

            update_passwd_box_texto = tk.Entry(add_window, show="*")
            update_passwd_box_texto.pack()

            save_button = tk.Button(add_window, text="Actualizar la contraseña", command=save_pass)
            save_button.pack()




