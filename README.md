# Gestor de Contraseñas con MySQL y Tkinter

Este es un proyecto de **Gestor de Contraseñas** que permite almacenar, actualizar y eliminar contraseñas asociadas a diferentes cuentas. Está desarrollado en Python utilizando **Tkinter** para la interfaz gráfica y **MySQL** como base de datos para gestionar de forma segura las contraseñas.

## Características

- **Interfaz Gráfica**: Implementada con Tkinter para una gestión fácil y visual de las contraseñas.
- **Almacenamiento seguro**: Utiliza MySQL para almacenar las contraseñas asociadas a diferentes cuentas.
- **Funciones de CRUD**: Puedes **Agregar**, **Actualizar**, **Eliminar** y **Mostrar** todas las cuentas con sus contraseñas.
- **Conexión a MySQL**: La base de datos está gestionada en un contenedor Docker de MySQL para mayor flexibilidad y portabilidad.

## Requisitos

- **Python 3.10+**
- **Tkinter** (preinstalado con Python en la mayoría de las distribuciones)
- **MySQL** (utilizado dentro de un contenedor Docker)
- **Docker Desktop** (para manejar el contenedor de MySQL)
- **Bibliotecas Python**:
  - `mysql-connector-python`
  - `tkinter`

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/Fernando-droidx/PassManager.git
   cd PassManager
2.  **Crear y activar un entorno virtual**:
    `python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate` 
    
3.  **Instalar dependencias**:
    
    `pip install mysql-connector-python` 
    
4.  **Configurar Docker para MySQL**:
    
    Si no tienes Docker, instálalo desde Docker Desktop. Luego ejecuta el siguiente comando para levantar el contenedor de MySQL:
    `docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=123456789 -e MYSQL_DATABASE=pass_manager -p 3306:3306 -d mysql:latest` 
    
    Este comando crea un contenedor de MySQL y establece una contraseña de root (`123456789`) con una base de datos llamada `pass_manager`.
    
5.  **Configurar la base de datos**:
    
    Abre MySQL dentro del contenedor:
    
    `docker exec -it mysql-container mysql -u root -p` 
    
    Luego ingresa la contraseña `123456789` y crea la tabla `cuentas`:
    
    `USE pass_manager;
    
    CREATE TABLE cuentas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre_cuenta VARCHAR(255) NOT NULL,
        contrasena VARCHAR(255) NOT NULL
    );` 
    
6.  **Ejecutar la aplicación**:
    
    Ejecuta la aplicación desde la terminal:
    
    `python main.py` 
    

## Uso

-   **Agregar una contraseña**:
    
    1.  Introduce el nombre de la cuenta (ej. Gmail, Facebook, etc.)
    2.  Introduce la contraseña asociada.
    3.  Haz clic en "Agregar" para almacenarla.
-   **Actualizar una contraseña**:
    
    1.  Introduce el nombre de la cuenta.
    2.  Introduce la nueva contraseña.
    3.  Haz clic en "Actualizar".
-   **Eliminar una cuenta**:
    
    1.  Introduce el nombre de la cuenta.
    2.  Haz clic en "Eliminar".
-   **Mostrar todas las cuentas**:
    
    -   Haz clic en "Mostrar cuentas" para ver una lista de todas las cuentas con sus contraseñas.

## Estructura del Proyecto


├── PassManager.py          # Lógica del gestor de contraseñas
├── main.py                 # Interfaz gráfica con Tkinter
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias del proyecto
└── .venv/                  # Entorno virtual (si lo configuras)` 

### `PassManager.py`

La clase **PassManager** contiene toda la lógica relacionada con la gestión de las contraseñas:

-   `agregar_pass(nombre_cuenta, contrasena)`: Agrega una nueva cuenta con su contraseña a la base de datos.
-   `actualizar_pass(nombre_cuenta, nueva_contrasena)`: Actualiza la contraseña para una cuenta específica.
-   `eliminar_pass(nombre_cuenta)`: Elimina una cuenta y su contraseña.
-   `obtener_cuentas()`: Devuelve una lista de todas las cuentas y sus contraseñas.

### `main.py`

Este archivo gestiona la interfaz gráfica del usuario (GUI) usando Tkinter:

-   **Entradas**: Para nombre de la cuenta y contraseña.
-   **Botones**: Agregar, Actualizar, Eliminar, Mostrar cuentas.
-   **Listbox**: Para mostrar todas las cuentas y contraseñas almacenadas.

## Personalización

Si deseas personalizar la paleta de colores o el diseño de la interfaz gráfica, puedes modificar las siguientes líneas en `main.py`:

`ventana.config(bg="#f5f5f5")  # Cambia el fondo de la ventana
btn_agregar.config(bg="#5c85d6", fg="white")  # Cambia el color de los botones
lista_cuentas.config(bg="#ffffff", fg="#333333")  # Cambia el estilo de la lista` 

## Docker

Este proyecto utiliza **Docker** para manejar la base de datos MySQL. Los comandos básicos que puedes usar son:

-   **Iniciar el contenedor**:

    
    `docker start mysql-container` 
    
-   **Detener el contenedor**:
    

    
    `docker stop mysql-container` 
    
-   **Eliminar el contenedor**:

    
    `docker rm -f mysql-container` 
    

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un _issue_ o envía un _pull request_ a este repositorio.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más información.

### Descripción del contenido:
- **Introducción**: Explicación breve del proyecto y sus características.
- **Requisitos**: Lista de dependencias y versiones necesarias para ejecutar el proyecto.
- **Instalación**: Instrucciones detalladas para configurar el entorno, levantar MySQL con Docker y ejecutar la aplicación.
- **Uso**: Explicación de las funciones principales de la aplicación.
- **Estructura del Proyecto**: Vista rápida de los archivos más importantes.
- **Docker**: Comandos para manejar el contenedor de MySQL.
- **Contribuciones y Licencia**: Información estándar para colaborar y la licencia del proyecto.

Este **README** cubre todas las áreas esenciales para que otros desarrolladores puedan entender y utilizar el proyecto sin problemas. ¡Espero que te sea útil!
