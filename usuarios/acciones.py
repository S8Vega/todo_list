import usuarios.usuario as modelo


class Acciones:
    def registro(self):
        print("vamos a registrarte en el sistema...")
        nombre = input("digita tu nombre: ")
        apellido = input("digita tu apellido: ")
        email = input("digita tu email: ")
        contrasena = input("digita tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellido, email, contrasena)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"perfecto, {nombre} te has registrado email {email}")
        else:
            print("no te has registrado correctamente")

    def login(self):
        print("identificate en el sistema: ")
        email = input("digita tu email: ")
        contrasena = input("digita tu contraseña: ")
        usuario = modelo.Usuario("", "", email, contrasena)
        login = usuario.identificar()
        if email == login[3]:
            print(f"bienvenido {login[1]}, te has registrado en el {login[5]}")
