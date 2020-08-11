import notas.nota as modelo

class Accion:
    def crear(self, usuario):
        print(f"{usuario[1]} vamos a crear una nueva nota")
        titulo = input("introduce el titulo de tu nota: ")
        descripcion = input("introduce la descripcion de tu nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion, False)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"has guardado la nota: {titulo}")
        else:
            print(f"no se ha guardado la nota {usuario[1]}")