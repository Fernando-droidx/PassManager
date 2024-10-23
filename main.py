import tkinter as tk
from tkinter import messagebox
import PassManager  # La clase PassManager que creamos

# Crear la instancia del gestor de contraseñas
pm = PassManager.PassManager()

# Funciones de la aplicación
def agregar_contrasena():
    nombre_cuenta = entrada_cuenta.get()
    contrasena = entrada_contrasena.get()
    if nombre_cuenta and contrasena:
        pm.agregar_pass(nombre_cuenta, contrasena)
        messagebox.showinfo("Éxito", f"Contraseña para {nombre_cuenta} agregada.")
        entrada_cuenta.delete(0, tk.END)
        entrada_contrasena.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Debe ingresar un nombre de cuenta y contraseña.")

def actualizar_contrasena():
    nombre_cuenta = entrada_cuenta.get()
    nueva_contrasena = entrada_contrasena.get()
    if nombre_cuenta and nueva_contrasena:
        pm.actualizar_pass(nombre_cuenta, nueva_contrasena)
        messagebox.showinfo("Éxito", f"Contraseña para {nombre_cuenta} actualizada.")
    else:
        messagebox.showerror("Error", "Debe ingresar un nombre de cuenta y una nueva contraseña.")

def eliminar_contrasena():
    nombre_cuenta = entrada_cuenta.get()
    if nombre_cuenta:
        pm.eliminar_pass(nombre_cuenta)
        messagebox.showinfo("Éxito", f"Cuenta {nombre_cuenta} eliminada.")
        entrada_cuenta.delete(0, tk.END)
        entrada_contrasena.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Debe ingresar el nombre de la cuenta para eliminar.")

def mostrar_cuentas():
    cuentas = pm.obtener_cuentas()
    lista_cuentas.delete(0, tk.END)
    for cuenta, contrasena in cuentas:
        lista_cuentas.insert(tk.END, f"{cuenta} -> {contrasena}")

ventana = tk.Tk()
ventana.title("Gestor de Contraseñas")
ventana.geometry("500x400")
ventana.config(bg="#f5f5f5")


frame_datos = tk.Frame(ventana, bg="#f5f5f5", padx=10, pady=10)
frame_datos.pack(pady=20)


tk.Label(frame_datos, text="Nombre de cuenta:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, sticky="e")
entrada_cuenta = tk.Entry(frame_datos, font=("Arial", 12), width=25)
entrada_cuenta.grid(row=0, column=1, padx=10, pady=5)


tk.Label(frame_datos, text="Contraseña:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, sticky="e")
entrada_contrasena = tk.Entry(frame_datos, font=("Arial", 12), width=25, show="*")
entrada_contrasena.grid(row=1, column=1, padx=10, pady=5)

frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=20)


btn_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_contrasena, font=("Arial", 12), bg="#5c85d6", fg="white", width=12, relief="flat")
btn_agregar.grid(row=0, column=0, padx=10, pady=5)


btn_actualizar = tk.Button(frame_botones, text="Actualizar", command=actualizar_contrasena, font=("Arial", 12), bg="#5c85d6", fg="white", width=12, relief="flat")
btn_actualizar.grid(row=0, column=1, padx=10, pady=5)


btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_contrasena, font=("Arial", 12), bg="#5c85d6", fg="white", width=12, relief="flat")
btn_eliminar.grid(row=0, column=2, padx=10, pady=5)


btn_mostrar = tk.Button(frame_botones, text="Mostrar cuentas", command=mostrar_cuentas, font=("Arial", 12), bg="#5c85d6", fg="white", width=36, relief="flat")
btn_mostrar.grid(row=1, column=0, columnspan=3, pady=10)

lista_cuentas = tk.Listbox(ventana, font=("Arial", 12), width=50, height=8, bg="#ffffff", fg="#333333", relief="flat", highlightthickness=1, highlightbackground="#5c85d6")
lista_cuentas.pack(pady=20)

# Ejecutar la interfaz
ventana.mainloop()
