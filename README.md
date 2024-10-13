# Password Manager

Este proyecto es una aplicación gráfica para la gestión de contraseñas, 
creada con `Tkinter` en Python. 
Permite agregar, eliminar y actualizar contraseñas todo guardado en un diccionario para que solo salga la cuenta asociada a la contraseña.

## Funcionalidades

- **Agregar Contraseña**: Permite al usuario ingresar una nueva contraseña y este la almacena en un diccionario, y se muestra en un listbox el nombre de la cuenta asociada a la contrasena.
- **Eliminar Contraseña**: El usuario puede seleccionar una contraseña del `Listbox` y eliminarla tanto de la interfaz como de la lista interna.
- **Actualizar Contraseña**: Permite seleccionar una contraseña existente, ingresar una nueva, y actualizarla tanto en la interfaz como en la lista interna.
  
## Estructura del Proyecto

- **Interfaz Gráfica**: Utiliza `Tkinter` para crear la ventana principal y gestionar la interacción del usuario.
- **Listbox**: Las contraseñas se muestran en el `Listbox` con asteriscos para ocultarlas, mientras que las contraseñas reales se almacenan en una lista interna.
- **Ventanas Secundarias**: Se utilizan ventanas emergentes para ingresar nuevas contraseñas o actualizar las existentes.

## Uso del Proyecto

### Requisitos

- Python 3.x
- Tkinter (viene preinstalado con Python)

### Instalación

1. Clona el repositorio o descarga el código fuente:
   ```bash
   git clone https://github.com/usuario/password-manager.git
2. Navega a la carpeta del proyecto:
    ```bash
   cd password-manager
3. Ejecuta el archivo principal del proyecto:
    ```bash
    python main.py
   
## Ejecución del Proyecto
Al ejecutar la aplicación, se abrirá una ventana principal con tres botones: Agregar, Eliminar y Actualizar.

### Agregar Contraseña:

Al hacer clic en "Agregar", se abrirá una ventana secundaria donde puedes ingresar una nueva contraseña. Esta se añadirá al Listbox el nombre de la cuenta, pero la contraseña real se almacenará en un valor de un map interno. y no se vera
### Eliminar Contraseña:

Selecciona una contraseña en el Listbox y presiona el botón "Eliminar". La contraseña seleccionada se eliminará de la interfaz y de la lista interna.
### Actualizar Contraseña:

Selecciona una contraseña en el Listbox, presiona "Actualizar" y se abrirá una ventana donde podrás ingresar una nueva contraseña. La contraseña se actualizará en la lista interna y se reflejará en el Listbox como una cadena de asteriscos.

### Mostrar Contraseña
Selecciona la contrasena que quieras ver y te la dara y solo tu la podras ver

## Contribuciones
Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature-branch).
Realiza tus cambios y haz commit (git commit -m 'Descripción del cambio').
Sube los cambios a tu rama (git push origin feature-branch).
Abre un Pull Request.
