from usuarios import acciones

print(
    """
Acciones disponibles:
    -registro
    -login
"""
)

hacer = acciones.Acciones()
accion = input("que quieres hacer?: ")

while accion != "registro" and accion != "login":
    accion = input("digita una accion valida: ")

if accion == "registro":
    hacer.registro()
if accion == "login":
    hacer.login()
