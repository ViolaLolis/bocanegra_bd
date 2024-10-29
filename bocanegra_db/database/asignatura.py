from database.config import obtener_conexion

class Asignatura:
    def __init__(self, nombre, ciclo, descripcion):
        self.nombre = nombre
        self.ciclo = ciclo
        self.descripcion = descripcion

    def insertar_asignatura(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO asignatura (nombre, ciclo, descripcion) VALUES (%s, %s, %s)"
        cursor.execute(query, (self.nombre, self.ciclo, self.descripcion))
        conexion.commit()
        cursor.close()
        conexion.close()
