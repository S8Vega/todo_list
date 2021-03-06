import notas.nota as modelo

class Accion:
    def crear(self, usuario):
        print(f"{usuario[1]} vamos a crear una nueva nota")
        titulo = input("introduce el titulo de tu nota: ")
        descripcion = input("introduce la descripcion de tu nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion, "0")
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"has guardado la nota: {titulo}")
        else:
            print(f"no se ha guardado la nota {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"{usuario[1]} aqui tienes tus notas: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        if len(notas) == 0:
            print("--------------------\n")
            print(f"{usuario[1]} no tienes notas todavia")
            print("--------------------\n")
        for nota in notas:
            print("--------------------\n")
            realizada ="NO" if nota[5] == 0 else "SI"
            print(f"titulo: {nota[2]} realizada = {realizada}")
            print(nota[3])
            print("--------------------\n")
            
    def borrar(self, usuario):
        titulo = input(f"{usuario[1]} introduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"hemos borrado la nota: {nota.titulo}")
        else:
            print("no se ha borrado la nota")

    def marcar(self, usuario):
        titulo = input(f"{usuario[1]} introduce el titulo de la nota a marcar: ")
        nota = modelo.Nota(usuario[0], titulo)
        marcada = nota.marcar()
        if marcada[0] >= 1:
            print(f"hemos marcado la nota: {nota.titulo}")
        else:
            print("no se ha marcado la nota")