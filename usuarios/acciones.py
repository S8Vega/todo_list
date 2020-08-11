import usuarios.usuario as modelo
import notas.acciones


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
            print(f"perfecto, {nombre} te has registrado con el email {email}")
        else:
            print("no te has registrado correctamente")

    def login(self):
        print("identificate en el sistema: ")
        try:
            email = input("digita tu email: ")
            contrasena = input("digita tu contraseña: ")
            usuario = modelo.Usuario("", "", email, contrasena)
            login = usuario.identificar()
            if email == login[3]:
                print(f"bienvenido {login[1]}, te has registrado en el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(e)
            print("login incorrecto")
    
    def proximasAcciones(self, usuario):
        print("""
        acciones disponibles:
            - crear nota (crear)
            - mostrar tus notas (mostrar)
            - eliminar nota (eliminar)
            - salir (salir)
        """)
        accion = input("que quieres hacer?: ")
        hacer = notas.acciones.Accion()
        if accion == "crear":
            print("vamos a crear")
            hacer.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("vamos a mostrar")
            hacer.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("vamos a eliminar")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"hasta pronto {usuario[1]}")
            exit()
        else:
            print("accion invalida")
            self.proximasAcciones(usuario)