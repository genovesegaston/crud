import mysql.connector

class Conexion:
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                user="root",
                password="root",
                host="127.0.0.1",
                database="clientesdb",
                port="3306"
            )
            
            print("Conexión establecida con éxito")
            
            return conexion
        
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos {}".format(error))

    ConexionBaseDeDatos()