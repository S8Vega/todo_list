import conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self, usuario_id, titulo = "", descripcion = "", realizada = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.realizada = str(realizada)
    
    def guardar(self):
        sql = f"SELECT * FROM notas WHERE usuarios_id = {self.usuario_id} AND titulo LIKE '{self.titulo}'"
        cursor.execute(sql)
        if cursor.rowcount > 0:
            print(f"la nota {self.titulo} ya esta registrada")
            return [0, self]
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW(), %s)"
        nota = (self.usuario_id, self.titulo, self.descripcion, self.realizada)
        cursor.execute(sql, nota)
        database.commit()
        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuarios_id = {self.usuario_id} ORDER BY `realizada` ASC"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def eliminar(self):
        sql = f"SELECT * FROM notas WHERE usuarios_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(sql)
        if cursor.rowcount > 1:
            print(f"el titulo {self.titulo} esta en varias notas, por favor se mas especifico")
            return [0, self]
        sql = f"DELETE FROM notas WHERE usuarios_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]
    
    def marcar(self):
        sql = f"SELECT * FROM notas WHERE usuarios_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(sql)
        if cursor.rowcount > 1:
            print(f"el titulo {self.titulo} esta en varias notas, por favor se mas especifico")
            return [0, self]
        sql = f"UPDATE notas SET realizada = '1' WHERE usuarios_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]