import mysql.connector

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456789',
            database='pass_manager',
            port=3306
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Ejecuta el código
conexion = conectar_db()
if conexion:
    cursor = conexion.cursor()
    cursor.execute("SHOW TABLES;")
    for tabla in cursor:
        print(tabla)
    cursor.close()
    conexion.close()
