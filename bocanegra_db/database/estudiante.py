from database.config import obtener_conexion

class Estudiante:
    def __init__(self, nombre, direccion, n_matricula):
        self.nombre = nombre
        self.direccion = direccion
        self.n_matricula = n_matricula

    def insertar_estudiante(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO estudiante (nombre, direccion, numero_matricula) VALUES (%s, %s, %s)"
        cursor.execute(query, (self.nombre, self.direccion, self.n_matricula))
        conexion.commit()
        cursor.close()
        conexion.close()
