from Conexion import *

class Clientes:
    def ingresarClinetes(nombre:str,apellido:str,sexo:str):
        
        try:
            con = Conexion.ConexionBaseDeDatos()
            cursor = con.cursor()
            consultaSQL= "insert into usuarios values(null,%s,%s,%s);"
            
            valores = (nombre,apellido,sexo)
            
            cursor.execute(consultaSQL,valores)    
            con.commit()
            print(cursor.rowcount,"registro ingresado")
            
            con.close()
            
        except mysql.connector.Error as error:
            
            print("Error en la carga de datos {}".format(error))
            
    def consultarClientes():
        try:
            con = Conexion.ConexionBaseDeDatos()
            cursor = con.cursor()
            cursor.execute("select * from usuarios;")    
            resultado = cursor.fetchall()
            
            
            con.commit()
            con.close()
            return resultado
            
        except mysql.connector.Error as error:
            
            print("Error en la carga de datos {}".format(error))

clientes = Clientes.consultarClientes()

for cliente in clientes:
    (id,nombre,apellido,sexo) = cliente
    print(id,sexo)