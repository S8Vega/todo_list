import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self, usuario_id, titulo, descripcion, realizada):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.realizada = str(realizada)
    
    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW(), %s)"
        nota = (self.usuario_id, self.titulo, self.descripcion, self.realizada)
        cursor.execute(sql, nota)
        database.commit()
        return [cursor.rowcount, self]