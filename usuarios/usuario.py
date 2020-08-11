import datetime
import hashlib
import usuarios.conexion as cnx

conexion = cnx.conectar()
database = conexion[0]
cursor = conexion[1]


class Usuario:
    def __init__(self, nombre, apellido, email, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena

    def registrar(self):
        fecha = datetime.datetime.now()
        cifrado = hashlib.sha256()
        cifrado.update(self.contrasena.encode("utf8"))
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result

    def identificar(self):
        return self.nombre
