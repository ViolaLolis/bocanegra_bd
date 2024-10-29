from database.config import obtener_conexion

class Aula:
    def __init__(self, numero, planta='1', situacion='DISPONIBLE'):
        self.numero = numero
        self.planta = planta
        self.situacion = situacion

    def insertar_aula(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO aula (numero, planta, situacion) VALUES (%s, %s, %s)"
        cursor.execute(query, (self.numero, self.planta, self.situacion))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def consultar_aulas():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "SELECT * FROM aula"
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados

    @staticmethod
    def consultar_aula(aula_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "SELECT * FROM aula WHERE id = %s"
        cursor.execute(query, (aula_id,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado

    @staticmethod
    def actualizar_aula(aula_id, numero, planta, situacion):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "UPDATE aula SET numero = %s, planta = %s, situacion = %s WHERE id = %s"
        cursor.execute(query, (numero, planta, situacion, aula_id))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar_aula(aula_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM aula WHERE id = %s"
        cursor.execute(query, (aula_id,))
        conexion.commit()
        cursor.close()
        conexion.close()
