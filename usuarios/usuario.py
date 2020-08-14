import conexion
import datetime
import hashlib

cnc = conexion.conectar()
database = cnc[0]
cursor = cnc[1]


class Usuario:
    def __init__(self, nombre, apellido, email, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena

    def cifrar(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.contrasena.encode("utf8"))
        return cifrado.hexdigest()

    def registrar(self):
        sql = f"SELECT * FROM usuarios WHERE email = '{self.email}'"
        cursor.execute(sql)
        if cursor.rowcount > 1:
            print(f"el email {self.email} ya esta registrado")
            return [0, self]
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, self.cifrar(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND contrasena = %s"
        usuario = (self.email, self.cifrar())
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result

