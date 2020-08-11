import mysql.connector
import datetime

database = mysql.connector.connect(
    host="localhost", user="root", passwd="0000", database="todo_list", port=3306
)

cursor = database.cursor(buffered=True)


class Usuario:
    def __init__(self, nombre, apellido, email, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena

    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, self.contrasena, fecha)
        cursor.execute(sql, usuario)
        database.commit()
        return [cursor.rowcount, self]

    def identificar(self):
        return self.nombre
