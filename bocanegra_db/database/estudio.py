from database.config import obtener_conexion

class Estudio:
    def __init__(self, id_estudiante, id_asignatura, hora='08:00:00'):
        self.id_estudiante = id_estudiante
        self.id_asignatura = id_asignatura
        self.hora = hora

    def insertar_estudio(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO estudia (estudiante_id, asignatura_id, hora) VALUES (%s, %s, %s)"
        cursor.execute(query, (self.id_estudiante, self.id_asignatura, self.hora))
        conexion.commit()
        cursor.close()
        conexion.close()
