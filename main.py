import tkinter as tk
from functools import partial
import PassManager

if __name__ == '__main__':

    ventana = tk.Tk()
    ventana.title("Password Manager")
    ventana.geometry("600x400")

    label_bienvenida = tk.Label(ventana, text="Bienvenido a PassManager", font=("Helvetica"), padx=20, pady=20)
    label_bienvenida.pack()
    frame_botones = tk.Frame(ventana)

    lista = tk.Listbox(ventana)
    lista.pack(padx=20, pady=20)

    pm = PassManager.PassManager()
    boton_agregar = tk.Button(frame_botones, text="Agregar",font=("Helvetica"), command=partial(pm.agregar_pass, lista))
    boton_agregar.pack(side="left", padx=20, pady=20)

    boton_eliminar = tk.Button(
        frame_botones, text="Eliminar",font=("Helvetica"), command=partial(pm.eliminar_pass, lista))
    boton_eliminar.pack(side="left", padx=20, pady=20)

    boton_actualizar = tk.Button(
        frame_botones, text="Actualizar",font=("Helvetica"), command=partial(pm.actualizar_pass, lista))
    boton_actualizar.pack(side="left",padx=20, pady=20)


    boton_verpass = tk.Button(
        frame_botones,font=("Helvetica"), text="Ver la contrasena", command=partial(pm.show, lista))
    boton_verpass.pack(side="left",padx=20, pady=20)

    frame_botones.pack()


    ventana.mainloop()