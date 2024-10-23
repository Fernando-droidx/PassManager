import mysql.connector

class PassManager:
    def __init__(self):
        self.conexion = self.conectar_db()

    def conectar_db(self):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123456789',
                database='pass_manager'
            )
            if conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                return conexion
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def agregar_pass(self, nombre_cuenta, contrasena):
        try:
            cursor = self.conexion.cursor()
            query = "INSERT INTO cuentas (nombre_cuenta, contrasena) VALUES (%s, %s)"
            cursor.execute(query, (nombre_cuenta, contrasena))
            self.conexion.commit()
            cursor.close()
            print(f"Contraseña para {nombre_cuenta} agregada correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al agregar la cuenta: {e}")

    def actualizar_pass(self, nombre_cuenta, nueva_contrasena):
        try:
            cursor = self.conexion.cursor()
            query = "UPDATE cuentas SET contrasena = %s WHERE nombre_cuenta = %s"
            cursor.execute(query, (nueva_contrasena, nombre_cuenta))
            self.conexion.commit()
            cursor.close()
            print(f"Contraseña para {nombre_cuenta} actualizada correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al actualizar la contraseña: {e}")

    def eliminar_pass(self, nombre_cuenta):
        try:
            cursor = self.conexion.cursor()
            query = "DELETE FROM cuentas WHERE nombre_cuenta = %s"
            cursor.execute(query, (nombre_cuenta,))
            self.conexion.commit()
            cursor.close()
            print(f"Cuenta '{nombre_cuenta}' eliminada correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al eliminar la cuenta: {e}")

    def obtener_cuentas(self):
        try:
            cursor = self.conexion.cursor()
            query = "SELECT nombre_cuenta, contrasena FROM cuentas"
            cursor.execute(query)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except mysql.connector.Error as e:
            print(f"Error al obtener las cuentas: {e}")
            return []
